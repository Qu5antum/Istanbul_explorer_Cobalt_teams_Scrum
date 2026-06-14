from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import torch
import os
import sys
import faiss
import pickle

sys.path.insert(0, os.path.join(os.getcwd(), 'data'))

from transformers import BertTokenizer, BertForSequenceClassification
from sentence_transformers import SentenceTransformer
import numpy as np
from data.intent_dataset import INTENT_LABELS
from data.istanbul_documents import ISTANBUL_DOCS

app = FastAPI(
    title="İstanbul Şehir Rehberi API",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# --------------------------------------------------
# MODEL YÜKLEME
# --------------------------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

try:
    intent_tokenizer = BertTokenizer.from_pretrained("model/istanbul_intent")
    intent_model = BertForSequenceClassification.from_pretrained("model/istanbul_intent").to(device)
except Exception:
    intent_tokenizer = BertTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
    intent_model = BertForSequenceClassification.from_pretrained(
        "dbmdz/bert-base-turkish-cased", 
        num_labels=len(INTENT_LABELS)
    ).to(device)

intent_model.eval()
embed_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
faiss_index = faiss.read_index("rag_data/istanbul_index.faiss")

with open("rag_data/chunks.pkl", "rb") as f:
    rag_data = pickle.load(f)

all_chunks = rag_data["chunks"]
chunk_meta = rag_data["meta"]

ISTANBUL_DOCS_KEYS = list(ISTANBUL_DOCS.keys())
ISTANBUL_DOCS_VALUES = list(ISTANBUL_DOCS.values())
ISTANBUL_DOCS_EMBEDS = None

# --------------------------------------------------
# СЛОВАРИ ДЛЯ КРАСИВОГО ВЫВОДА
# --------------------------------------------------
INTENT_EMOJIS = {
    'tarih_ve_kultur': '🏛️',
    'ulasim_ve_seyahat': '🚇',
    'yemek_ve_gastronomi': '🍽️',
    'cografya_ve_semt': '🗺️',
    'egitim_ve_is': '🎓',
    'spor_ve_eglence': '⚽',
}

INTENT_ACIKLAMA = {
    'tarih_ve_kultur': 'Tarih & Kültür',
    'ulasim_ve_seyahat': 'Ulaşım & Seyahat',
    'yemek_ve_gastronomi': 'Yemek & Gastronomi',
    'cografya_ve_semt': 'Coğrafya & Semt',
    'egitim_ve_is': 'Eğitim & İş',
    'spor_ve_eglence': 'Spor & Eğlence',
}

OFF_TOPIC_SOURCES = {
    'kayit_yenileme',
    'sinav_sistemi',
    'burslar_indirimler',
    'mezuniyet_sartlari',
    'ogrenci_hizmetleri',
    'akademik_takvim',
    'disiplin_ve_kurallar',
    'erasmus_uluslararasi',
    'ois_teknik_destek',
    'kampus_ve_ulasim',
    'yurt_ve_konaklama',
}

ISTANBUL_FALLBACK = (
    "Bu sohbet asistanı İstanbul şehir rehberidir. "
    "İstanbul hakkında turizm, ulaşım, yemek, tarih, semtler ve kültür bilgisi verebilirim. "
    "Topkapı Üniversitesi ya da kampüs içi detaylar gibi özel eğitim kurumlarına ait bilgiler bu kapsamın dışındadır."
)

# --------------------------------------------------
# SCHEMA
# --------------------------------------------------
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    intent: str
    confidence: float

# --------------------------------------------------
# ФУНКЦИИ ЛОГИКИ
# --------------------------------------------------
def detect_intent(text):
    enc = intent_tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128,
        padding="max_length"
    ).to(device)

    with torch.no_grad():
        logits = intent_model(**enc).logits[0]

    probs = torch.softmax(logits, dim=0).cpu().numpy()
    best_idx = int(probs.argmax())
    
    return INTENT_LABELS[best_idx], float(probs[best_idx])

def retrieve_context(query, k=3):
    q_vec = embed_model.encode([query]).astype("float32")
    distances, indices = faiss_index.search(q_vec, k)
    
    results = []
    for dist, idx in zip(distances[0], indices[0]):
        results.append({
            "metin": all_chunks[idx],
            "kaynak": chunk_meta[idx].get("kaynak", "Bilinmeyen Kaynak"),
            "dist": float(dist)
        })
    return results

def chatbot_logic(message):
    raw_intent, score = detect_intent(message)
    retrieved = retrieve_context(message)

    filtered = [r for r in retrieved if r["kaynak"] not in OFF_TOPIC_SOURCES]

    # Eğer tüm sonuçlar eğitim kurumuna özel kaynaklarsa, İstanbul içeriğiyle yanıtlayalım
    if not filtered:
        answer = ISTANBUL_FALLBACK
        return answer, f"🤖 {INTENT_ACIKLAMA.get(raw_intent, raw_intent)}", score

    # Преобразуем технический интент в красивый вид с эмодзи
    emoji = INTENT_EMOJIS.get(raw_intent, '🤖')
    text_intent = INTENT_ACIKLAMA.get(raw_intent, raw_intent)
    pretty_intent = f"{emoji} {text_intent}"

    cevap = ""
    kaynaklar = set()

    # Собираем контекст из top-2 результатов, off-topic kaynakları hariç tutuyoruz
    for r in filtered[:2]:
        cevap += r["metin"].strip() + "\n\n"
        if r["kaynak"]:
            kaynaklar.add(r["kaynak"])

    # Красиво добавляем источники в конец ответа
    if kaynaklar:
        cevap += "📍 **Kaynaklar:** " + ", ".join(kaynaklar)

    return cevap.strip(), pretty_intent, score

# --------------------------------------------------
# ENDPOINTS
# --------------------------------------------------
@app.get("/")
def root():
    return {"message": "İstanbul Şehir Rehberi API çalışıyor"}

@app.get("/app")
def app_ui():
    return FileResponse(os.path.join("static", "index.html"))

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer, intent, confidence = chatbot_logic(request.message)
    return ChatResponse(
        answer=answer,
        intent=intent,
        confidence=confidence
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)