from fastapi import FastAPI
from pydantic import BaseModel
import torch
import faiss
import pickle
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), 'data'))

from transformers import BertTokenizer, BertForSequenceClassification
from sentence_transformers import SentenceTransformer
from data.intent_dataset import INTENT_LABELS

app = FastAPI(
    title="İstanbul Şehir Rehberi API",
    version="1.0.0"
)

# --------------------------------------------------
# MODEL YÜKLEME
# --------------------------------------------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

try:
    intent_tokenizer = BertTokenizer.from_pretrained(
        "model/istanbul_intent"
    )

    intent_model = BertForSequenceClassification.from_pretrained(
        "model/istanbul_intent"
    ).to(device)

except Exception:

    intent_tokenizer = BertTokenizer.from_pretrained(
        "dbmdz/bert-base-turkish-cased"
    )

    intent_model = BertForSequenceClassification.from_pretrained(
        "dbmdz/bert-base-turkish-cased",
        num_labels=len(INTENT_LABELS)
    ).to(device)

intent_model.eval()

embed_model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)

faiss_index = faiss.read_index(
    "rag_data/istanbul_index.faiss"
)

with open("rag_data/chunks.pkl", "rb") as f:
    rag_data = pickle.load(f)

all_chunks = rag_data["chunks"]
chunk_meta = rag_data["meta"]

# --------------------------------------------------
# EMOJİLER
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
# FONKSİYONLAR
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

    return (
        INTENT_LABELS[best_idx],
        float(probs[best_idx])
    )


def retrieve_context(query, k=3):

    q_vec = embed_model.encode([query]).astype("float32")

    distances, indices = faiss_index.search(q_vec, k)

    results = []

    for dist, idx in zip(distances[0], indices[0]):
        results.append({
            "metin": all_chunks[idx],
            "kaynak": chunk_meta[idx]["kaynak"],
            "dist": float(dist)
        })

    return results


def chatbot_logic(message):

    intent, score = detect_intent(message)

    retrieved = retrieve_context(message)

    cevap = ""

    for r in retrieved[:2]:
        cevap += r["metin"][:400] + "\n\n"

    return cevap, intent, score

# --------------------------------------------------
# API ENDPOINTS
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "İstanbul Şehir Rehberi API çalışıyor"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer, intent, confidence = chatbot_logic(
        request.message
    )

    return ChatResponse(
        answer=answer,
        intent=intent,
        confidence=confidence
    )