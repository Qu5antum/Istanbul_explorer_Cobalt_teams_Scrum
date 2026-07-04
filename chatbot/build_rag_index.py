# -*- coding: utf-8 -*-
"""
İstanbul Şehir Rehberi - RAG İndeks Oluşturma
Bu script, data/istanbul_documents.py içindeki gerçek İstanbul verisinden
FAISS vektör indeksi ve chunks.pkl dosyasını oluşturur.

NOT: Önceki rag_data/ klasöründeki indeks yanlışlıkla bir üniversite
(kayıt, sınav, yurt vb.) veri setinden oluşturulmuştu. Bu script onu
gerçek İstanbul içeriğiyle (tarih, ulaşım, gezilecek yerler, parklar,
gastronomi vb.) değiştirir.

Çalıştırmak için:
    python build_rag_index.py
"""

import os
import re
import pickle
import sys

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

sys.path.insert(0, os.path.join(os.getcwd(), "data"))
from data.istanbul_documents import ISTANBUL_DOCS

OUT_DIR = "rag_data"
os.makedirs(OUT_DIR, exist_ok=True)


def split_into_chunks(text, max_chars=350):
    """Metni cümle sınırlarına saygı duyarak parçalara böler."""
    text = text.strip()
    sentences = re.split(r"(?<=[.!?])\s+", text)

    chunks = []
    current = ""
    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue
        if len(current) + len(sent) + 1 <= max_chars:
            current = (current + " " + sent).strip()
        else:
            if current:
                chunks.append(current)
            current = sent
    if current:
        chunks.append(current)
    return chunks


def main():
    print("📚 İstanbul belgelerinden chunk'lar oluşturuluyor...")
    all_chunks = []
    chunk_meta = []

    for kaynak, text in ISTANBUL_DOCS.items():
        for chunk in split_into_chunks(text):
            all_chunks.append(chunk)
            chunk_meta.append({"kaynak": kaynak})

    print(f"✅ Toplam {len(all_chunks)} chunk oluşturuldu ({len(ISTANBUL_DOCS)} kategoriden).")

    print("🧠 Embedding modeli yükleniyor (paraphrase-multilingual-MiniLM-L12-v2)...")
    embed_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    print("🔢 Embedding'ler hesaplanıyor...")
    embeddings = embed_model.encode(
        all_chunks,
        convert_to_numpy=True,
        show_progress_bar=True,
    ).astype("float32")

    dim = embeddings.shape[1]
    print(f"📐 Embedding boyutu: {dim}")

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss_path = os.path.join(OUT_DIR, "istanbul_index.faiss")
    faiss.write_index(index, faiss_path)
    print(f"💾 FAISS indeksi kaydedildi: {faiss_path}")

    chunks_path = os.path.join(OUT_DIR, "chunks.pkl")
    with open(chunks_path, "wb") as f:
        pickle.dump({"chunks": all_chunks, "meta": chunk_meta}, f)
    print(f"💾 Chunks kaydedildi: {chunks_path}")

    print("\n🎉 RAG indeksi başarıyla yeniden oluşturuldu. Artık İstanbul içeriğini kullanıyor.")

    # ---- Eşik kalibrasyonu için tanı (diagnostik) ----
    print("\n🔍 Eşik kalibrasyonu için örnek mesafeler:")
    test_queries_in_topic = [
        "Topkapı Sarayı nerede?",
        "İstanbul'da nerede gezinebilirim?",
        "Beyoğlu'nda gezilecek yerler nelerdir?",
        "Kadıköy'de ne yapılır?",
    ]
    test_queries_off_topic = [
        "Borç nasıl pişirilir?",
        "Python'da liste nasıl sıralanır?",
        "Bugün hava nasıl olacak Moskova'da?",
        "En iyi futbol oyuncusu kim?",
    ]

    def show_distances(label, queries):
        print(f"\n  {label}:")
        for q in queries:
            qv = embed_model.encode([q]).astype("float32")
            d, i = index.search(qv, 1)
            print(f"    '{q}' → en yakın mesafe: {d[0][0]:.3f}")

    show_distances("İstanbul ile ilgili sorular", test_queries_in_topic)
    show_distances("İstanbul ile ilgisiz sorular", test_queries_off_topic)

    print(
        "\nℹ️  chatbot_app.py içindeki RELEVANCE_DISTANCE_THRESHOLD değerini, "
        "yukarıdaki iki grup arasında net bir ayrım sağlayacak şekilde ayarlayın "
        "(genelde 'ilgili' grubun en yüksek değeri ile 'ilgisiz' grubun en düşük "
        "değeri arasında bir sayı seçin)."
    )


if __name__ == "__main__":
    main()
