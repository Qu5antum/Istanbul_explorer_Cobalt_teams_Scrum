# -*- coding: utf-8 -*-
"""
🕌 İstanbul Şehir Rehberi Chatbot
RAG + BERT Fine-Tuned Intent Detection
"""

import gradio as gr
import torch
import faiss
import pickle
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), 'data'))

# ─── Model Yükleme ───────────────────────────────────────────
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"🖥️  Cihaz: {device}")

from transformers import BertTokenizer, BertForSequenceClassification
from sentence_transformers import SentenceTransformer
from data.intent_dataset import INTENT_LABELS

print("🔄 BERT Intent modeli yükleniyor...")
try:
    intent_tokenizer = BertTokenizer.from_pretrained('model/istanbul_intent')
    intent_model = BertForSequenceClassification.from_pretrained('model/istanbul_intent').to(device)
    print("✅ Fine-tuned model yüklendi!")
except Exception as e:
    print(f"⚠️  Fine-tuned model yok ({e}), base model kullanılıyor...")
    intent_tokenizer = BertTokenizer.from_pretrained('dbmdz/bert-base-turkish-cased')
    intent_model = BertForSequenceClassification.from_pretrained(
        'dbmdz/bert-base-turkish-cased',
        num_labels=len(INTENT_LABELS),
        id2label={i: l for i, l in enumerate(INTENT_LABELS)},
        label2id={l: i for i, l in enumerate(INTENT_LABELS)}
    ).to(device)

intent_model.eval()

print("🔄 RAG bileşenleri yükleniyor...")
embed_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
faiss_index = faiss.read_index('rag_data/istanbul_index.faiss')
with open('rag_data/chunks.pkl', 'rb') as f:
    rag_data = pickle.load(f)
    all_chunks = rag_data['chunks']
    chunk_meta = rag_data['meta']

print(f"✅ Hazır! FAISS: {faiss_index.ntotal} vektör\n")

# ─── Intent ve Kategori Emojileri ───────────────────────────
INTENT_EMOJIS = {
    'tarih_ve_kultur'    : '🏛️',
    'ulasim_ve_seyahat'  : '🚇',
    'yemek_ve_gastronomi': '🍽️',
    'cografya_ve_semt'   : '🗺️',
    'egitim_ve_is'       : '🎓',
    'spor_ve_eglence'    : '⚽',
}

INTENT_ACIKLAMA = {
    'tarih_ve_kultur'    : 'Tarih & Kültür',
    'ulasim_ve_seyahat'  : 'Ulaşım & Seyahat',
    'yemek_ve_gastronomi': 'Yemek & Gastronomi',
    'cografya_ve_semt'   : 'Coğrafya & Semt',
    'egitim_ve_is'       : 'Eğitim & İş',
    'spor_ve_eglence'    : 'Spor & Eğlence',
}

# ─── Çekirdek Fonksiyonlar ───────────────────────────────────
def detect_intent(text):
    enc = intent_tokenizer(
        text, return_tensors='pt',
        truncation=True, max_length=128, padding='max_length'
    ).to(device)
    with torch.no_grad():
        logits = intent_model(**enc).logits[0]
    probs = torch.softmax(logits, dim=0).cpu().numpy()
    best_idx = int(probs.argmax())
    return INTENT_LABELS[best_idx], float(probs[best_idx])


def retrieve_context(query, k=3):
    q_vec = embed_model.encode([query]).astype('float32')
    distances, indices = faiss_index.search(q_vec, k)
    results = []
    for dist, idx in zip(distances[0], indices[0]):
        results.append({
            'metin' : all_chunks[idx],
            'kaynak': chunk_meta[idx]['kaynak'],
            'dist'  : float(dist),
        })
    return results


def chatbot_logic(message, history):
    message = message.strip()
    if not message:
        return "Lütfen bir soru yazın. 😊"

    intent, score = detect_intent(message)
    retrieved = retrieve_context(message, k=3)

    emoji = INTENT_EMOJIS.get(intent, '🔍')
    konu  = INTENT_ACIKLAMA.get(intent, intent)
    kaynaklar = list({r['kaynak'].replace('_', ' ').title() for r in retrieved})

    cevap  = f"{emoji} **Konu:** {konu} *(Güven: %{score*100:.0f})*\n"
    cevap += f"📚 **Kaynak:** {', '.join(kaynaklar)}\n\n---\n\n"

    for r in retrieved[:2]:
        metin = r['metin'].strip()[:400]
        cevap += f"📍 {metin}...\n\n"

    cevap += "---\n*Daha fazla bilgi için başka bir soru sorabilirsiniz! 🕌*"
    return cevap


# ─── Gradio UI ───────────────────────────────────────────────
theme = gr.themes.Soft(primary_hue="red", secondary_hue="slate").set(
    button_primary_background_fill="*primary_500",
)

with gr.Blocks(theme=theme, title="İstanbul Şehir Rehberi") as demo:
    gr.HTML("""
    <div style='text-align:center; padding:10px 0'>
        <h1 style='color:#c0392b; font-size:2em; margin:0'>🕌 İstanbul Şehir Rehberi</h1>
        <p style='color:#7f8c8d; margin:5px 0'>
            RAG + BERT destekli akıllı şehir asistanı
        </p>
    </div>
    """)

    gr.ChatInterface(
        fn=chatbot_logic,
        chatbot=gr.Chatbot(height=500, label="İstanbul Asistanı"),
        textbox=gr.Textbox(
            placeholder="İstanbul hakkında bir şeyler sorun... (tarih, ulaşım, yemek, spor...)",
            container=False, scale=7
        ),
        examples=[
            "Ayasofya ne zaman inşa edildi ve nasıl bir tarihi var?",
            "İstanbul'da metro ile Asya yakasına geçebilir miyim?",
            "İstanbul'da mutlaka yenmesi gereken yemekler neler?",
            "Boğaz kaç kilometre uzunluğunda?",
            "Galatasaray UEFA Kupası'nı hangi yıl aldı?",
            "İstanbul'daki en önemli üniversiteler hangileri?",
        ],
    )

    gr.HTML("""
    <div style='text-align:center; color:#95a5a6; font-size:0.85em; padding:10px'>
        🏛️ Tarih &nbsp;|&nbsp; 🚇 Ulaşım &nbsp;|&nbsp; 🍽️ Gastronomi &nbsp;|&nbsp; 
        🗺️ Coğrafya &nbsp;|&nbsp; 🎓 Eğitim &nbsp;|&nbsp; ⚽ Spor
    </div>
    """)

if __name__ == '__main__':
    demo.launch(server_port=7860, share=False)
