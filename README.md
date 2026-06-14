# Istanbul Explorer

İstanbul'a yeni gelen kullanıcılar için geliştirilen, ilgi çekici mekanları keşfetmeye, kişiselleştirilmiş gezi rotaları oluşturmaya ve yapay zeka destekli bir şehir asistanıyla etkileşime girmeye yarayan tam kapsamlı bir web uygulaması.

Bu proje **EFC312 Yazılım Proje Geliştirme** dersi kapsamında geliştirilmiştir.

---

## İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Mimari](#mimari)
- [Veritabanı Tasarımı](#veritabanı-tasarımı)
- [UML Diyagramları](#uml-diyagramları)
- [API Dokümantasyonu](#api-dokümantasyonu)
- [Kurulum](#kurulum)
- [Proje Yapısı](#proje-yapısı)
- [Ekip](#ekip)

---

## Proje Hakkında

Istanbul Explorer, İstanbul'u ziyaret eden veya şehre yeni taşınan kullanıcıların şehri kolayca keşfetmesine yardımcı olmak için tasarlanmıştır. Kullanıcılar kategori bazlı mekanlara göz atabilir, konumlarına yakın yerleri bulabilir, mekanlara yorum ve puan bırakabilir, favori mekanlarını kaydedebilir ve bütçelerine/ilgi alanlarına göre otomatik olarak optimize edilmiş gezi rotaları oluşturabilirler. Ayrıca proje, RAG (Retrieval-Augmented Generation) ve BERT tabanlı bir yapay zeka sohbet asistanı içerir, bu asistan İstanbul hakkında sorulan sorulara belge tabanlı yanıtlar verir.

Sistem üç ana bileşenden oluşur:

| Bileşen | Açıklama |
|---|---|
| `backend/` | FastAPI tabanlı REST API, PostgreSQL veritabanı, JWT kimlik doğrulama |
| `frontend/` | HTML/CSS/JavaScript tabanlı kullanıcı arayüzü |
| `chatbot/` | RAG + BERT Fine-Tuning ile geliştirilmiş İstanbul şehir rehberi sohbet botu |

---

## Özellikler

### Kullanıcı İşlemleri
- E-posta, telefon numarası ve şifre ile kayıt olma
- JWT tabanlı giriş (OAuth2 Password Flow)
- Rol tabanlı yetkilendirme (`admin` / `user`)

### Mekan Keşfi
- Tüm mekanları listeleme
- Kategoriye göre filtreleme (kafe, müze, park, restoran vb.)
- Başlığa göre mekan arama
- Kullanıcının konumuna göre yakındaki mekanları bulma (mesafe hesaplama ile)
- Yakındaki mekanları kategoriye göre filtreleme
- Mekan detayları: açıklama, adres, fiyat aralığı, görsel, koordinatlar

### Etkileşim
- Mekanlara yorum yazma ve görüntüleme
- Mekanlara 1-5 arası puan verme / güncelleme
- Mekanların ortalama puanını görme
- Mekanları favorilere ekleme / çıkarma
- Favori mekanları listeleme

### Rota Oluşturma
- Seçilen kategorilere ve bütçeye göre otomatik rota oluşturma
- En yakın komşu (nearest neighbor) algoritmasıyla rota optimizasyonu
- Her durak için varış/kalkış saati, seyahat süresi ve ziyaret süresi hesaplama
- Kullanıcının tüm rotalarını listeleme
- Rota detaylarını (sıralı mekan listesi) görüntüleme
- Rota silme
- Paylaşılabilir bağlantı (share token) ile rotayı herkese açık görüntüleme

### Admin İşlemleri
- Yeni mekan oluşturma, güncelleme, silme
- Yeni kategori oluşturma

### AI Sohbet Asistanı (Chatbot)
- BERT tabanlı niyet (intent) sınıflandırma — 6 sınıf, 130+ örnek
- RAG (FAISS + Sentence Transformers) ile İstanbul hakkında 20 kategoride belge tabanlı bilgi getirme
- Gradio arayüzü üzerinden etkileşim

---

## Kullanılan Teknolojiler

### Backend
| Teknoloji | Amaç |
|---|---|
| **Python 3** | Ana programlama dili |
| **FastAPI 0.136** | Asenkron REST API framework |
| **Uvicorn** | ASGI sunucusu |
| **SQLAlchemy 2.0** (async) | ORM |
| **Alembic** | Veritabanı migration yönetimi |
| **PostgreSQL** (asyncpg) | İlişkisel veritabanı |
| **Pydantic / pydantic-settings** | Veri doğrulama ve ayar yönetimi |
| **python-jose** | JWT token oluşturma/doğrulama |
| **passlib + argon2-cffi** | Şifre hashleme |

### Frontend
| Teknoloji | Amaç |
|---|---|
| **HTML5 / CSS3** | Sayfa yapısı ve stil |
| **Vanilla JavaScript (ES Modules)** | API entegrasyonu, dinamik içerik |
| **Fetch API** | Backend ile HTTP iletişimi |
| **LocalStorage** | JWT token saklama |

### Chatbot / AI
| Teknoloji | Amaç |
|---|---|
| **Turkish BERT** (`dbmdz/bert-base-turkish-cased`) | Niyet (intent) sınıflandırma |
| **Sentence Transformers** (`paraphrase-multilingual-MiniLM-L12-v2`) | Embedding üretimi |
| **FAISS (IndexFlatL2)** | Vektör arama / RAG retriever |
| **Hugging Face Transformers / Datasets** | Model eğitimi ve veri yönetimi |
| **Gradio** | Sohbet botu web arayüzü |
| **Jupyter Notebook** | Geliştirme ve deney ortamı |

---

## Mimari

Sistem üç katmanlı bir mimariye sahiptir: istemci tarafı (frontend), uygulama sunucusu (FastAPI backend) ve veri/AI servisleri.

```
┌──────────────────────────┐
│        Frontend          │
│   HTML / CSS / JS (ES)    │
│  - Sayfa yönlendirme      │
│  - LocalStorage (JWT)     │
└────────────┬──────────────┘
             │ REST (fetch, JSON)
             ▼
┌──────────────────────────┐
│        Backend (FastAPI)  │
│  ┌──────────────────────┐ │
│  │   API Endpoints       │ │   /api/user, /api/place,
│  │   (Routers)           │ │   /api/category, /api/route,
│  └──────────┬────────────┘ │   /api/place/{id}/comment, ...
│  ┌──────────▼────────────┐ │
│  │   Services            │ │   İş mantığı (rota optimizasyonu,
│  │                        │ │   bütçe filtreleme, yetkilendirme)
│  └──────────┬────────────┘ │
│  ┌──────────▼────────────┐ │
│  │   Repositories         │ │   Veritabanı erişim katmanı
│  └──────────┬────────────┘ │
│  ┌──────────▼────────────┐ │
│  │   SQLAlchemy Models    │ │
│  └──────────┬────────────┘ │
└─────────────┼──────────────┘
              ▼
┌──────────────────────────┐
│       PostgreSQL           │
└──────────────────────────┘

┌──────────────────────────┐
│   Chatbot (ayrı servis)    │
│  BERT Intent + FAISS RAG   │
│  Gradio arayüzü            │
└──────────────────────────┘
```

Backend katmanlı (layered) bir mimari izler:

1. **Endpoints** — HTTP isteklerini karşılar, dependency injection ile servis ve kimlik doğrulama bağımlılıklarını alır.
2. **Services** — İş mantığını içerir (örneğin rota optimizasyonu, bütçe filtreleme, favori kontrolü).
3. **Repositories** — Veritabanı CRUD işlemlerini soyutlar (`BaseRepository` üzerinden generic işlemler).
4. **Models** — SQLAlchemy ORM modelleri ve tablo ilişkileri.
5. **Exception Handlers** — Özel hata sınıfları (`PlaceNotFoundException`, `RouteAlreadyExists`, `AccessException` vb.) merkezi olarak `BaseAppException` üzerinden yakalanır ve standart JSON hata yanıtına dönüştürülür.

### Kimlik Doğrulama Akışı

- Kullanıcı `/api/user/login` ile giriş yapar (OAuth2 Password Flow — `username` alanı e-posta olarak kullanılır).
- Şifre `argon2` ile hashlenmiş haliyle karşılaştırılır.
- Başarılı girişte `role` ve `sub` (kullanıcı id) bilgisini içeren bir JWT döner.
- Korumalı endpointler `require_roles(...)` dependency'si ile bu token'ı doğrular ve role bazlı erişim kontrolü yapar (`ADMIN`, `USER`).

---

## Veritabanı Tasarımı

Veritabanı 8 ana tablodan oluşur: `users`, `places`, `categories`, `comments`, `place_ratings`, `favorite_places`, `routes`, `route_places` ve `places`–`categories` arasındaki çoka-çok ilişkiyi kuran `place_category` ara tablosu.

### Tablolar ve Alanları

**users**
| Alan | Tip | Açıklama |
|---|---|---|
| id | UUID (PK) | Birincil anahtar |
| email | string (unique) | Giriş için kullanılır |
| phone_number | string (unique, nullable) | |
| password | string | Argon2 ile hashlenmiş |
| is_active | bool | Hesap aktiflik durumu |
| role | enum (`admin`, `user`) | Yetkilendirme |
| created_at | datetime | |

**places**
| Alan | Tip | Açıklama |
|---|---|---|
| id | int (PK) | |
| title | string | Mekan adı |
| link | string | Harici bağlantı |
| price | string | Fiyat aralığı (örn. `"50-150"` veya `"Free"`) |
| latitude / longitude | float | Koordinatlar |
| address | string | |
| description | string | |
| image_path | string | |
| created_at | datetime | |

**categories**
| Alan | Tip | Açıklama |
|---|---|---|
| id | int (PK) | |
| title | string | Kategori adı (Cafe, Museum, Park, Restaurant vb.) |
| created_at | datetime | |

**comments**
| Alan | Tip | Açıklama |
|---|---|---|
| id | int (PK) | |
| title | string | Yorum metni |
| place_id | int (FK → places) | |
| user_id | UUID (FK → users) | |
| created_at | datetime | |

**place_ratings**
| Alan | Tip | Açıklama |
|---|---|---|
| id | int (PK) | |
| rating | int (1-5) | |
| place_id | int (FK → places) | |
| user_id | UUID (FK → users) | Benzersiz: bir kullanıcı bir mekana tek puan verebilir |
| created_at | datetime | |

**favorite_places**
| Alan | Tip | Açıklama |
|---|---|---|
| id | int (PK) | |
| user_id | UUID (FK → users) | |
| place_id | int (FK → places) | Benzersiz: kullanıcı+mekan kombinasyonu |
| created_at | datetime | |

**routes**
| Alan | Tip | Açıklama |
|---|---|---|
| id | int (PK) | |
| user_id | UUID (FK → users) | |
| title | string | Rota başlığı (benzersiz) |
| total_distance | float | Toplam mesafe (km) |
| estimated_duration | int | Tahmini süre (dakika) |
| share_token | UUID (unique) | Paylaşım bağlantısı için |
| is_public | bool | |
| created_at | datetime | |

**route_places**
| Alan | Tip | Açıklama |
|---|---|---|
| id | int (PK) | |
| route_id | int (FK → routes) | |
| place_id | int (FK → places) | |
| order_number | int | Ziyaret sırası |
| title | string | |
| arrival_time / departure_time | datetime | |
| travel_duration | int | Önceki duraktan seyahat süresi (dk) |
| visit_duration | int | Mekanda geçirilecek süre (dk) |
| created_at | datetime | |

### İlişkiler

- Bir **kullanıcı** birden çok yorum, puan, rota ve favori mekana sahip olabilir (1-N).
- Bir **mekan** birden çok yorum, puan, favori kaydı ve rota durağına sahip olabilir (1-N).
- Bir **mekan** birden çok **kategoriye** ait olabilir ve bir kategori birden çok mekanı kapsayabilir (N-N, `place_category` ara tablosu üzerinden).
- Bir **rota** birden çok **route_place** (durak) içerir (1-N) ve her durak tek bir mekana referans verir.

---

## UML Diyagramları

Bu bölümde projenin UML diyagramları için kullanılabilecek bir özet bulunmaktadır. Diyagramların görsel (SVG/PNG) versiyonları `docs/diagrams/` klasörüne eklenmesi önerilir.

### ER Diyagramı (Varlık-İlişki)

```
users ──1───N── comments ──N───1── places
  │                                    │
  ├──1───N── place_ratings ──N───1────┤
  │                                    │
  ├──1───N── favorite_places ──N───1──┤
  │                                    │
  └──1───N── routes ──1───N── route_places ──N───1── places

places ──N───N── categories  (place_category)
```

### Class Diagram (Özet)

```
User
 ├─ id, email, phone_number, password, is_active, role, created_at
 ├─ comments: list[Comment]
 ├─ ratings: list[PlaceRating]
 └─ routes: list[Route]

Place
 ├─ id, title, link, price, latitude, longitude, address, description, image_path
 ├─ categories: list[Category]
 ├─ comments: list[Comment]
 ├─ ratings: list[PlaceRating]
 └─ route_places: list[RoutePlace]

Category
 ├─ id, title
 └─ places: list[Place]

Route
 ├─ id, user_id, title, total_distance, estimated_duration, share_token, is_public
 └─ route_places: list[RoutePlace]

RoutePlace
 ├─ id, route_id, place_id, order_number, title
 └─ arrival_time, departure_time, travel_duration, visit_duration

Comment / PlaceRating / FavoritePlace
 └─ user_id (FK), place_id (FK), ek alanlar
```

### Use Case Diyagramı (Özet)

**Aktörler:** Ziyaretçi (User), Yönetici (Admin)

| Aktör | Use Case'ler |
|---|---|
| User | Kayıt ol, Giriş yap, Mekanları görüntüle/ara/filtrele, Yakındaki mekanları bul, Mekan detayına git, Yorum yap, Puan ver, Favorilere ekle/çıkar, Rota oluştur, Rotalarını görüntüle/sil, Rota paylaş |
| Admin | (User'ın tüm yetkileri) + Mekan oluştur/güncelle/sil, Kategori oluştur |

### Sequence Diagram — Rota Oluşturma (Özet)

```
Kullanıcı → Frontend: "Rota Oluştur" formunu doldur ve gönder
Frontend → API (/api/route/generate): POST (kategori_id'leri, bütçe, konum, başlangıç zamanı)
API → RouteService: generate_route(data, user)
RouteService → RouteRepository: aynı başlıkta rota var mı kontrol et
RouteService → CategoryRepository: kategorileri doğrula
RouteService → PlaceRepository: konuma yakın, kategoriye uygun mekanları getir
RouteService → RouteService: bütçeye göre filtrele
RouteService → RouteService: en yakın komşu algoritmasıyla rotayı optimize et
RouteService → RouteService: zaman çizelgesi oluştur (varış/kalkış saatleri)
RouteService → RouteRepository: Route ve RoutePlace kayıtlarını oluştur
RouteRepository → PostgreSQL: INSERT
API → Frontend: rota detaylarını JSON olarak döndür
Frontend → Kullanıcı: oluşturulan rotayı haritada/listede göster
```

### Activity Diagram — Rota Oluşturma Akışı (Özet)

```
[Başla]
  → Kullanıcı bilgileri gir (başlık, kategori, bütçe, konum, başlangıç zamanı)
  → Aynı başlıkta rota var mı?
       Evet → Hata döndür (RouteAlreadyExists) → [Bitir]
       Hayır ↓
  → Seçilen kategoriler veritabanında mevcut mu?
       Hayır → Hata döndür (SomeCategoryNotFound) → [Bitir]
       Evet ↓
  → Konuma yakın ve kategoriye uygun mekanları getir
  → Bütçe belirtildi mi?
       Evet → Bütçeye uygun mekanları filtrele
       Hayır ↓
  → En yakın komşu algoritmasıyla rota sırasını belirle
  → Her durak için varış/kalkış saatlerini hesapla
  → Route ve RoutePlace kayıtlarını veritabanına yaz
  → Sonucu kullanıcıya döndür
[Bitir]
```

---

## API Dokümantasyonu

Tüm endpointler `/api` prefix'i ile başlar. Backend çalıştırıldığında otomatik oluşturulan Swagger UI dokümantasyonuna `http://127.0.0.1:8000/docs` adresinden ulaşılabilir.

### Kimlik Doğrulama (`/api/user`)

| Method | Endpoint | Açıklama | Yetki |
|---|---|---|---|
| POST | `/api/user/register` | Yeni kullanıcı kaydı | Herkese açık |
| POST | `/api/user/login` | Giriş (OAuth2 Password Flow) → JWT döner | Herkese açık |

### Kategoriler (`/api`)

| Method | Endpoint | Açıklama | Yetki |
|---|---|---|---|
| GET | `/api/category` | Tüm kategorileri listele | Herkese açık |
| POST | `/api/admin/category/create` | Yeni kategori oluştur | Admin |

### Mekanlar (`/api`)

| Method | Endpoint | Açıklama | Yetki |
|---|---|---|---|
| GET | `/api/place/all` | Tüm mekanları listele | Herkese açık |
| POST | `/api/place/nearby` | Kullanıcı konumuna yakın mekanları getir | User / Admin |
| POST | `/api/place/nearby/category/{category_id}` | Yakındaki mekanları kategoriye göre filtrele | User / Admin |
| POST | `/api/place/{place_id}` | Mekan detayını getir (mesafe dahil) | Admin |
| GET | `/api/search/{title}` | Başlığa göre mekan ara | User / Admin |
| GET | `/api/category/{category_id}` | Kategoriye göre mekanları getir | User / Admin |
| POST | `/api/admin/place/create` | Yeni mekan oluştur | Admin |
| PUT | `/api/admin/place/{place_id}/update` | Mekanı güncelle | Admin |
| DELETE | `/api/admin/delete_place` | Mekanı sil | Admin |

### Yorumlar (`/api`)

| Method | Endpoint | Açıklama | Yetki |
|---|---|---|---|
| GET | `/api/place/{place_id}/comment/` | Mekana ait yorumları getir | User / Admin |
| POST | `/api/place/{place_id}/comment/create/` | Mekana yorum ekle | User / Admin |

### Puanlama (`/api`)

| Method | Endpoint | Açıklama | Yetki |
|---|---|---|---|
| POST | `/api/place/{place_id}/rate` | Mekana puan ver / güncelle (1-5) | User / Admin |
| GET | `/api/place/{place_id}/rating` | Mekanın puan bilgisini getir | User / Admin |

### Favoriler (`/api`)

| Method | Endpoint | Açıklama | Yetki |
|---|---|---|---|
| GET | `/api/user/favorites` | Kullanıcının favori mekanlarını getir | User / Admin |
| POST | `/api/place/{place_id}/favorite` | Mekanı favorilere ekle | User / Admin |
| DELETE | `/api/place/{place_id}/favorite` | Mekanı favorilerden çıkar | User / Admin |

### Rotalar (`/api`)

| Method | Endpoint | Açıklama | Yetki |
|---|---|---|---|
| POST | `/api/route/generate` | Kategori, bütçe ve konuma göre rota oluştur | User / Admin |
| GET | `/api/route/all` | Kullanıcının tüm rotalarını listele | User / Admin |
| GET | `/api/route/{route_id}/route_places` | Rotaya ait durakları getir | User / Admin |
| DELETE | `/api/route/{route_id}/delete` | Rotayı sil | User / Admin |
| GET | `/api/route/{route_token}/shared` | Paylaşım token'ı ile rotayı görüntüle | User / Admin |

### Örnek İstek — Rota Oluşturma

```http
POST /api/route/generate
Authorization: Bearer <token>
Content-Type: application/json

{
  "route_title": "Tarihi Yarımada Turu",
  "start_time": "2025-06-01T09:00:00Z",
  "budget": 500,
  "userLocation": {
    "lat": 41.0082,
    "lng": 28.9784
  },
  "category_ids": [1, 3, 4]
}
```

**Yanıt**

```json
{
  "route_id": 12,
  "title": "Tarihi Yarımada Turu",
  "places": [
    {
      "order": 1,
      "title": "Ayasofya",
      "arrival_time": "2025-06-01T09:00:00Z",
      "departure_time": "2025-06-01T11:00:00Z"
    },
    {
      "order": 2,
      "title": "Topkapı Sarayı",
      "arrival_time": "2025-06-01T11:08:00Z",
      "departure_time": "2025-06-01T13:08:00Z"
    }
  ]
}
```

### Hata Yanıtları

API, özel exception sınıfları üzerinden standart bir hata formatı döner:

```json
{
  "error": "Konum bulunmadı"
}
```

Başlıca özel hatalar: `PlaceNotFoundException`, `PlaceAlreadyExists`, `PlaceAlreadyInFavorite`, `RouteNotFound`, `RouteAlreadyExists`, `SomeCategoryNotFound`, `CategoryAlreadyExists`, `UserNotFoundException`, `UserAlreadyExists`, `UnauthorizedException`, `AccessException`, `DatabaseException`.

---

## Kurulum

### Gereksinimler
- Python 3.11+
- PostgreSQL
- Node.js (opsiyonel, frontend için statik sunucu)

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

`.env` dosyası oluşturun:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=istanbul_explorer

SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Veritabanı migration'larını uygulayın:

```bash
alembic upgrade head
```

Sunucuyu başlatın:

```bash
python -m src.main
# veya
uvicorn src.main:app --reload
```

API artık `http://127.0.0.1:8000` adresinde çalışır. Swagger dokümantasyonu: `http://127.0.0.1:8000/docs`

### Frontend

```bash
cd frontend/src/pages
# Herhangi bir statik dosya sunucusu ile çalıştırın, örn:
python -m http.server 5500
```

Tarayıcıda `http://127.0.0.1:5500/index.html` adresini açın.

> `frontend/src/scripts/api.js` dosyasındaki `API_URL` değişkeninin backend adresiyle eşleştiğinden emin olun (`http://127.0.0.1:8000/api`).

### Chatbot

```bash
cd chatbot
pip install -r requirements.txt
python chatbot_app.py
```

Gradio arayüzü `http://localhost:7860` adresinde açılır.

---

## Proje Yapısı

```
EFC312_Yazilim_Proje_gelistirme/
├── backend/
│   ├── src/
│   │   ├── api/
│   │   │   ├── endpoints/        # FastAPI router'ları
│   │   │   ├── schemas/          # Pydantic şemaları
│   │   │   └── dependencies/     # Auth & rol kontrolü
│   │   ├── auth/                 # JWT oluşturma/doğrulama
│   │   ├── core/                 # Ayarlar (config.py)
│   │   ├── database/             # Modeller, DB bağlantısı
│   │   ├── exception_handlers/   # Özel hata sınıfları
│   │   ├── repositories/         # Veritabanı erişim katmanı
│   │   ├── services/             # İş mantığı
│   │   └── main.py               # Uygulama giriş noktası
│   ├── migrations/                # Alembic migration dosyaları
│   ├── images/                    # Statik mekan görselleri
│   └── requirements.txt
│
├── frontend/
│   └── src/
│       ├── pages/                # HTML sayfaları (login, mekanlar, rotalar vb.)
│       └── scripts/               # api.js, auth.js
│
├── chatbot/
│   ├── data/                      # İstanbul belgeleri ve intent veri seti
│   ├── chatbot_app.py             # Gradio uygulaması
│   ├── BERT_FineTuning.ipynb
│   ├── RAG_Pipeline.ipynb
│   └── requirements.txt
│
└── README.md
```

---

## Ekip

| Rol | Sorumluluk |
|---|---|
| Backend Geliştirici | FastAPI mimarisi, veritabanı tasarımı, rota algoritması, JWT kimlik doğrulama |
| Frontend Geliştirici | HTML/CSS/JS arayüzü, API entegrasyonu |
| AI / Chatbot Geliştirici | BERT fine-tuning, RAG pipeline, Gradio arayüzü |
| QA / Dokümantasyon | API testleri, README ve teknik dokümantasyon |

---

## Lisans

Bu proje **EFC312 Yazılım Proje Geliştirme** dersi kapsamında eğitim amaçlı geliştirilmiştir.