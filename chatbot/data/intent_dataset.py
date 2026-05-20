# -*- coding: utf-8 -*-
"""
İstanbul Chatbot - Intent (Niyet) Veri Seti
Fine-tuning için etiketlenmiş soru-cevap çiftleri
"""

INTENT_LABELS = [
    "tarih_ve_kultur",       # Tarihi mekanlar, Osmanlı, Bizans
    "ulasim_ve_seyahat",     # Metro, vapur, uçuş, köprüler
    "yemek_ve_gastronomi",   # Restoranlar, yöresel yemekler, çarşılar
    "cografya_ve_semt",      # İlçeler, Boğaz, Asya-Avrupa yakası
    "egitim_ve_is",          # Üniversiteler, iş hayatı, ekonomi
    "spor_ve_eglence",       # Futbol, konserler, müzeler
]

LABEL_TO_ID = {label: idx for idx, label in enumerate(INTENT_LABELS)}
ID_TO_LABEL = {idx: label for label, idx in LABEL_TO_ID.items()}

RAW_DATA = [
    # ─── tarih_ve_kultur ───
    ("Ayasofya ne zaman inşa edildi?", "tarih_ve_kultur"),
    ("Topkapı Sarayı nerede?", "tarih_ve_kultur"),
    ("Mavi Cami'nin kaç minaresi var?", "tarih_ve_kultur"),
    ("Bizans imparatorluğu İstanbul'u ne zaman kaybetti?", "tarih_ve_kultur"),
    ("İstanbul'un tarihi surları hakkında bilgi verir misin?", "tarih_ve_kultur"),
    ("Kapalıçarşı'da ne satılır?", "tarih_ve_kultur"),
    ("Galata Kulesi nasıl bir yapı?", "tarih_ve_kultur"),
    ("Osmanlı İstanbul'u ne zaman fethetti?", "tarih_ve_kultur"),
    ("Yerebatan Sarnıcı nedir?", "tarih_ve_kultur"),
    ("İstanbul hangi imparatorlukların başkentiydi?", "tarih_ve_kultur"),
    ("Sultanahmet'te gezilecek yerler nelerdir?", "tarih_ve_kultur"),
    ("Fatih Sultan Mehmet'in İstanbul'la ilgisi nedir?", "tarih_ve_kultur"),
    ("Kariye Camii nerede?", "tarih_ve_kultur"),
    ("Eyüp Sultan Camii nereden geçiyor?", "tarih_ve_kultur"),
    ("Süleymaniye Camii'ni kim yaptırdı?", "tarih_ve_kultur"),
    ("Beyoğlu'nun tarihi nedir?", "tarih_ve_kultur"),
    ("Mısır Çarşısı'nda ne satılır?", "tarih_ve_kultur"),
    ("Hippodrom Meydanı nedir?", "tarih_ve_kultur"),
    ("Bizans döneminden kalma yapılar hangileri?", "tarih_ve_kultur"),
    ("Konstantinopolis kimdi?", "tarih_ve_kultur"),
    ("Theodosius Surları ne zaman yapıldı?", "tarih_ve_kultur"),
    ("Türk kahvesinin UNESCO ile ilişkisi nedir?", "tarih_ve_kultur"),
    ("Pera semti İstanbul'un neresi?", "tarih_ve_kultur"),
    ("Kapalıçarşı ne zaman kuruldu?", "tarih_ve_kultur"),
    ("Fener Rum Patrikhanesi nerede?", "tarih_ve_kultur"),

    # ─── ulasim_ve_seyahat ───
    ("İstanbul'da metro nasıl kullanılır?", "ulasim_ve_seyahat"),
    ("Avrupa'dan Asya'ya nasıl geçilir?", "ulasim_ve_seyahat"),
    ("Metrobüs hangi hatta çalışıyor?", "ulasim_ve_seyahat"),
    ("İstanbul Havalimanı'na nasıl gidilir?", "ulasim_ve_seyahat"),
    ("Vapur nereden kalkar?", "ulasim_ve_seyahat"),
    ("Marmaray nedir?", "ulasim_ve_seyahat"),
    ("Adalara nasıl gidilir?", "ulasim_ve_seyahat"),
    ("Boğaz'dan geçiş köprüleri hangileri?", "ulasim_ve_seyahat"),
    ("Sabiha Gökçen Havalimanı nerede?", "ulasim_ve_seyahat"),
    ("İstanbul trafik durumu nedir?", "ulasim_ve_seyahat"),
    ("Kabataş'tan Taksim'e nasıl gidilir?", "ulasim_ve_seyahat"),
    ("İstanbul kart nedir, nasıl alınır?", "ulasim_ve_seyahat"),
    ("Galata Köprüsü nereden geçiyor?", "ulasim_ve_seyahat"),
    ("Nostalji tramvayı nerede?", "ulasim_ve_seyahat"),
    ("Boğaz vapuru seferleri nasıl?", "ulasim_ve_seyahat"),
    ("Havalimanından şehir merkezine ulaşım?", "ulasim_ve_seyahat"),
    ("Tünel nedir, nerede?", "ulasim_ve_seyahat"),
    ("İstanbul'da taksi nasıl çağrılır?", "ulasim_ve_seyahat"),
    ("T1 tramvay hattı nereden nereye gider?", "ulasim_ve_seyahat"),
    ("Yavuz Sultan Selim Köprüsü nerede?", "ulasim_ve_seyahat"),
    ("Boğaz'da deniz taksi var mı?", "ulasim_ve_seyahat"),
    ("İstanbul'da bisiklet kiralama nerede?", "ulasim_ve_seyahat"),
    ("Şehir Hatları vapurları ne zaman kalkar?", "ulasim_ve_seyahat"),

    # ─── yemek_ve_gastronomi ───
    ("İstanbul'da ne yenmeli?", "yemek_ve_gastronomi"),
    ("Balık ekmek nerede satılır?", "yemek_ve_gastronomi"),
    ("İstanbul'un meşhur yemekleri nelerdir?", "yemek_ve_gastronomi"),
    ("Kumpir nerede yenir?", "yemek_ve_gastronomi"),
    ("Türk kahvaltısı nasıl olur?", "yemek_ve_gastronomi"),
    ("Kadıköy'deki iyi restoranlar?", "yemek_ve_gastronomi"),
    ("İstanbul'da meze kültürü nedir?", "yemek_ve_gastronomi"),
    ("Kokoreç nedir, nerede yenir?", "yemek_ve_gastronomi"),
    ("Midye dolma nereden alınır?", "yemek_ve_gastronomi"),
    ("Simit nasıl bir yiyecektir?", "yemek_ve_gastronomi"),
    ("Türk çayı kültürü nedir?", "yemek_ve_gastronomi"),
    ("İstanbul'da Michelin yıldızlı restoran var mı?", "yemek_ve_gastronomi"),
    ("Mısır Çarşısı'nda ne yenir?", "yemek_ve_gastronomi"),
    ("Bağdat Caddesi'ndeki kafeler?", "yemek_ve_gastronomi"),
    ("İstanbul'da deniz ürünleri nerede yenir?", "yemek_ve_gastronomi"),
    ("İstanbul mutfağı hangi mutfaklardan etkilenmiş?", "yemek_ve_gastronomi"),
    ("Lüfer balığı nedir?", "yemek_ve_gastronomi"),
    ("Galata'da kahve içmek için nereler önerilir?", "yemek_ve_gastronomi"),
    ("Beyoğlu'nda akşam yemeği için neresi iyi?", "yemek_ve_gastronomi"),
    ("İstanbul'a özgü tatlılar nelerdir?", "yemek_ve_gastronomi"),
    ("Balık Pazarı İstanbul'da nerede?", "yemek_ve_gastronomi"),

    # ─── cografya_ve_semt ───
    ("İstanbul Boğazı ne uzunluğunda?", "cografya_ve_semt"),
    ("Avrupa ve Asya yakası arasındaki fark ne?", "cografya_ve_semt"),
    ("Haliç nedir?", "cografya_ve_semt"),
    ("İstanbul kaç ilçeden oluşur?", "cografya_ve_semt"),
    ("Kız Kulesi nerede?", "cografya_ve_semt"),
    ("Boğaz'ın en dar yeri neresi?", "cografya_ve_semt"),
    ("Bebek semti nerede?", "cografya_ve_semt"),
    ("Çamlıca Tepesi kaç metre yükseklikte?", "cografya_ve_semt"),
    ("Büyükçekmece ile Küçükçekmece arasındaki fark?", "cografya_ve_semt"),
    ("Prens Adaları kaç adadan oluşur?", "cografya_ve_semt"),
    ("Boğaziçi neden stratejik öneme sahip?", "cografya_ve_semt"),
    ("Üsküdar nerede, hangi yakada?", "cografya_ve_semt"),
    ("Karaköy ile Eminönü arasındaki mesafe?", "cografya_ve_semt"),
    ("İstanbul'un Avrupa yakasında hangi ilçeler var?", "cografya_ve_semt"),
    ("Marmara Denizi ile Karadeniz nasıl bağlanıyor?", "cografya_ve_semt"),
    ("İstanbul Belgrad Ormanı nerede?", "cografya_ve_semt"),
    ("Florya sahili nerede?", "cografya_ve_semt"),
    ("İstanbul'un en kalabalık ilçesi hangisi?", "cografya_ve_semt"),
    ("Poyraz rüzgarı ne anlama geliyor?", "cografya_ve_semt"),
    ("Büyükada'ya vapur ne kadar sürer?", "cografya_ve_semt"),
    ("Emirgan Korusu nerede?", "cografya_ve_semt"),
    ("İstanbul'un iklimi nasıldır?", "cografya_ve_semt"),

    # ─── egitim_ve_is ───
    ("İstanbul'daki üniversiteler hangileri?", "egitim_ve_is"),
    ("Boğaziçi Üniversitesi nerede?", "egitim_ve_is"),
    ("İTÜ ne zaman kuruldu?", "egitim_ve_is"),
    ("İstanbul ekonominin önemi nedir?", "egitim_ve_is"),
    ("Borsa İstanbul nedir?", "egitim_ve_is"),
    ("Robert Kolej ne kadar eskidir?", "egitim_ve_is"),
    ("Levent iş merkezi nerede?", "egitim_ve_is"),
    ("İstanbul'da teknoloji şirketleri var mı?", "egitim_ve_is"),
    ("Türkiye'nin en büyük şirketi İstanbul'da mı?", "egitim_ve_is"),
    ("İstanbul Üniversitesi'nin tarihi?", "egitim_ve_is"),
    ("Trendyol ve Getir İstanbul'dan mı?", "egitim_ve_is"),
    ("Koç Üniversitesi nerede?", "egitim_ve_is"),
    ("Teknopark İstanbul ne yapar?", "egitim_ve_is"),
    ("Sabancı Üniversitesi İstanbul'da mı?", "egitim_ve_is"),
    ("İstanbul'un en büyük ekonomik sektörü nedir?", "egitim_ve_is"),
    ("İstanbul'da turizm sektörünün boyutu?", "egitim_ve_is"),
    ("Yıldız Teknik Üniversitesi nerede?", "egitim_ve_is"),
    ("İstanbul kaç turist çekiyor?", "egitim_ve_is"),
    ("İstanbul'da iş kurmak kolay mı?", "egitim_ve_is"),
    ("Marmara Üniversitesi kaç öğrenciye sahip?", "egitim_ve_is"),

    # ─── spor_ve_eglence ───
    ("Galatasaray'ın tarihi nedir?", "spor_ve_eglence"),
    ("Fenerbahçe'nin stadyumu nerede?", "spor_ve_eglence"),
    ("Beşiktaş taraftarları hangi stadı kullanıyor?", "spor_ve_eglence"),
    ("İstanbul Maratonu ne zaman yapılır?", "spor_ve_eglence"),
    ("Formula 1 İstanbul'da yapılıyor mu?", "spor_ve_eglence"),
    ("Türkiye'nin en büyük camisi nerede?", "spor_ve_eglence"),
    ("İstanbul'da müzeler hangileri?", "spor_ve_eglence"),
    ("İstanbul Bienali nedir?", "spor_ve_eglence"),
    ("İstanbul Modern nerede?", "spor_ve_eglence"),
    ("İstanbul'da gece hayatı nerede?", "spor_ve_eglence"),
    ("UEFA Şampiyonlar Ligi İstanbul'da yapıldı mı?", "spor_ve_eglence"),
    ("Zorlu PSM nedir?", "spor_ve_eglence"),
    ("Galatasaray UEFA kupasını aldı mı?", "spor_ve_eglence"),
    ("Pera Müzesi ne tür eserlere sahip?", "spor_ve_eglence"),
    ("İstanbul Jazz Festivali ne zaman?", "spor_ve_eglence"),
    ("Türkiye Süper Ligi'nde hangi İstanbul takımları var?", "spor_ve_eglence"),
    ("Arkeoloji Müzesi İstanbul'da mı?", "spor_ve_eglence"),
    ("Rahmi Koç Müzesi ne tür bir müze?", "spor_ve_eglence"),
    ("İstanbul'da basketbol takımları var mı?", "spor_ve_eglence"),
    ("Lale Festivali nerede yapılır?", "spor_ve_eglence"),
    ("İstanbul'da konser nerede izlenir?", "spor_ve_eglence"),
    ("Sakıp Sabancı Müzesi nerede?", "spor_ve_eglence"),
]

if __name__ == "__main__":
    import pandas as pd
    df = pd.DataFrame(RAW_DATA, columns=["metin", "intent"])
    print(f"✅ Toplam örnek: {len(df)}")
    print(f"🏷️  Sınıf sayısı: {df['intent'].nunique()}")
    print()
    print(df["intent"].value_counts())
