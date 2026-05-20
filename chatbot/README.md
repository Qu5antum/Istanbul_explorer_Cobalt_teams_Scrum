# 🕌 İstanbul Şehir Rehberi Chatbot

RAG (Retrieval-Augmented Generation) + BERT Fine-Tuning ile geliştirilmiş
**İstanbul şehrine özel** akıllı chatbot projesi.

---

## 📁 Proje Yapısı

```
istanbul_chatbot/
├── data/
│   ├── istanbul_documents.py   # 20 kategorili İstanbul bilgi veri seti
│   └── intent_dataset.py       # 130+ etiketli soru (6 intent sınıfı)
│
├── rag_data/                   # (otomatik oluşturulur)
│   ├── istanbul_dataset/       # HuggingFace Dataset
│   ├── istanbul_index.faiss    # FAISS vektör indeksi
│   └── chunks.pkl              # Metin parçaları
│
├── model/                      # (otomatik oluşturulur)
│   └── istanbul_intent/        # Fine-tuned BERT modeli
│
├── 00_Veri_Seti_Hazirlik.ipynb     # Veri seti oluşturma ve keşif
├── 01_RAG_Pipeline.ipynb           # Embedding + FAISS indeks oluşturma
├── 02_BERT_Mimarisi.ipynb          # BERT analizi ve görselleştirme
├── 03_BERT_FineTuning.ipynb        # Intent detection model eğitimi
├── 04_RAG_BERT_Entegrasyon.ipynb   # Tam sistem + Gradio arayüzü
└── chatbot_app.py                  # Standalone chatbot uygulaması
```

---

## 🗂️ Veri Seti

### İstanbul Belgeleri (20 Kategori)
| Kategori | İçerik |
|----------|--------|
| `tarih_ve_kuruluş` | Byzantion, Konstantinopolis, Osmanlı dönemi |
| `cografya_ve_konumu` | Boğaz, Haliç, ilçeler, adalar |
| `nufus_ve_demographics` | Nüfus verileri, ilçe büyüklükleri |
| `ekonomi_ve_is_hayati` | BIST, ticaret, finans merkezi |
| `tarihi_yarimada_ve_surlar` | Theodosius Surları, UNESCO alanları |
| `ayasofya` | Tarihi, mimarisi, önemi |
| `topkapi_sarayi` | Osmanlı sarayı, koleksiyonlar |
| `mavi_cami_sultanahmet` | Sultanahmet Camii detayları |
| `kapalicarsi` | Grand Bazaar, tarih ve alışveriş |
| `bogaz_ve_uskudar_besiktas` | Boğaz semtleri |
| `ulasim` | Metro, vapur, Marmaray, havalimanı |
| `egitim_ve_universiteler` | İTÜ, Boğaziçi, Marmara vb. |
| `kultur_sanat_muzeler` | Müzeler, festivaller, sanat |
| `gastronomi_ve_yemek_kulturu` | Yemekler, çarşılar, lezzetler |
| `beyoglu_ve_istiklal` | Beyoğlu, Galata, Taksim |
| `kadikoy_ve_asya_yakasi` | Kadıköy, Üsküdar, Bağdat Caddesi |
| `dogal_alanlar_ve_parklar` | Ormanlar, parklar, sahiller |
| `iklim` | Mevsimler, rüzgarlar, sıcaklık |
| `spor` | Futbol, F1, maraton |
| `teknoloji_ve_girisimcilik` | Startup ekosistemi, unicornlar |
| `dini_mekanlar_ve_kiliseler` | Camiler, kiliseler, sinagoglar |
| `ada_ve_marmara` | Prens Adaları |
| `genel_bilgiler` | Özet bilgiler |

### Intent Sınıfları (6 Sınıf, 130+ Örnek)
```
tarih_ve_kultur       → 25 örnek
ulasim_ve_seyahat     → 23 örnek
yemek_ve_gastronomi   → 21 örnek
cografya_ve_semt      → 22 örnek
egitim_ve_is          → 20 örnek
spor_ve_eglence       → 22 örnek
```

---

## 🚀 Kurulum ve Çalıştırma

### 1. Ortam Kurulumu
```bash
pip install datasets transformers torch sentence-transformers \
            faiss-cpu scikit-learn pandas numpy matplotlib seaborn \
            gradio tqdm
```

### 2. Adım Adım Çalıştırma

```bash
# Sırayla notebook'ları çalıştırın:
jupyter notebook 00_Veri_Seti_Hazirlik.ipynb   # Veri seti oluştur
jupyter notebook 01_RAG_Pipeline.ipynb          # FAISS indeksi oluştur
jupyter notebook 02_BERT_Mimarisi.ipynb         # BERT analizi (isteğe bağlı)
jupyter notebook 03_BERT_FineTuning.ipynb       # Modeli eğit
jupyter notebook 04_RAG_BERT_Entegrasyon.ipynb  # Chatbot başlat
```

### 3. Standalone Uygulama
```bash
python chatbot_app.py
# → http://localhost:7860
```

---

## 🤖 Sistem Mimarisi

```
Kullanıcı Sorusu
      │
      ▼
┌─────────────────────┐
│  BERT Intent Detect │  ← Fine-tuned Turkish BERT
│  (6 sınıf)          │
└─────────────────────┘
      │ intent + güven skoru
      ▼
┌─────────────────────┐
│  RAG Retriever      │  ← Sentence Transformers + FAISS
│  FAISS L2 Search    │
└─────────────────────┘
      │ ilgili metin parçaları
      ▼
┌─────────────────────┐
│  Response Builder   │  ← Belge tabanlı yanıt
│  (Kaynak gösterimi) │
└─────────────────────┘
      │
      ▼
  Kullanıcıya Yanıt
```

---

## 📊 Kullanılan Modeller
- **BERT**: `dbmdz/bert-base-turkish-cased` (Turkish BERT)
- **Embedding**: `paraphrase-multilingual-MiniLM-L12-v2`
- **Vector DB**: FAISS (IndexFlatL2)

---

*🕌 İstanbul — Üç imparatorluğun başkenti, bir dünyanın kalbi.*
