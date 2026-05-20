# -*- coding: utf-8 -*-
"""
İstanbul Şehri - Kapsamlı Bilgi Veri Seti
RAG Pipeline için hazırlanmıştır.
"""

ISTANBUL_DOCS = {

    "tarih_ve_kuruluş": """
İstanbul, dünyanın en köklü ve tarihi şehirlerinden biridir. Şehir, MÖ 657 yılında Megaralı kolonistler tarafından Byzantion adıyla kurulmuştur. 
Kuruluş efsanesine göre kenti, Kral Byzas kurmuş ve kendi adını vermiştir. 
Roma İmparatoru Konstantin, MS 330 yılında şehri yeniden inşa ederek başkent ilan etmiş ve Konstantinopolis adını vermiştir.
Bizans İmparatorluğu'nun başkenti olarak yaklaşık 1000 yıl boyunca Hristiyan dünyasının merkezi olmuştur.
29 Mayıs 1453'te Fatih Sultan Mehmet komutasındaki Osmanlı ordusu şehri fethederek İstanbul adını vermiştir.
Bu tarih Türk tarihinin en önemli dönüm noktalarından biri olarak kabul edilmektedir.
Osmanlı İmparatorluğu'nun başkenti olarak yaklaşık 470 yıl boyunca hizmet vermiştir.
Cumhuriyet döneminde başkentlik görevi Ankara'ya devredilmiş olsa da İstanbul ekonomik ve kültürel başkent olmaya devam etmektedir.
Şehir, tarihte Byzantion, Konstantinopolis, Kostantiniyye ve İstanbul gibi çeşitli isimlerle anılmıştır.
İstanbul, üç büyük imparatorluğun —Roma, Bizans ve Osmanlı— başkentliğini yapmış tek şehirdir.
""",

    "cografya_ve_konumu": """
İstanbul, Türkiye'nin kuzeybatısında, Marmara Bölgesi'nde yer almaktadır.
Şehir, İstanbul Boğazı (Boğaziçi) tarafından ikiye ayrılarak hem Avrupa hem de Asya kıtalarında konumlanmaktadır.
Avrupa yakası Trakya yarımadasında, Asya yakası ise Anadolu'dadır.
İstanbul, dünyada iki kıtaya yayılan az sayıdaki şehirden biridir.
Şehrin kuzeyinde Karadeniz, güneyinde Marmara Denizi yer almaktadır.
İstanbul Boğazı, Karadeniz ile Marmara Denizi'ni birbirine bağlayan yaklaşık 31 km uzunluğundaki su yoludur.
Haliç (Golden Horn), Avrupa yakasında tarihi yarımadayı çevreleyen doğal bir körfezdir.
Şehrin toplam yüzölçümü yaklaşık 5.461 km² olup 39 ilçeden oluşmaktadır.
Karadeniz kıyısındaki ilçeler Beykoz, Şile, Arnavutköy ve Sarıyer'dir.
Marmara kıyısında ise Kadıköy, Maltepe, Kartal, Pendik, Tuzla, Büyükçekmece gibi ilçeler yer almaktadır.
Boğaz boyunca uzanan semtler arasında Bebek, Rumelihisarı, Emirgan, Tarabya ve Sarıyer sayılabilir.
İstanbul Adaları (Prens Adaları), Marmara Denizi'nde şehre bağlı 9 adadan oluşan ilçedir.
Büyükada, Heybeliada, Burgazada ve Kınalıada bu adaların en büyükleridir.
""",

    "nufus_ve_demographics": """
İstanbul, Türkiye'nin en kalabalık şehri ve Avrupa'nın en büyük şehridir.
2024 verilerine göre İstanbul'un nüfusu yaklaşık 15-16 milyon kişiye ulaşmıştır.
Büyük şehir bölgesiyle birlikte nüfusun 20 milyonun üzerinde olduğu tahmin edilmektedir.
Türkiye nüfusunun yaklaşık yüzde 20'si İstanbul'da yaşamaktadır.
Şehir, Türkiye'nin dört bir yanından göç alan bir metropoldür.
En kalabalık ilçeler Bağcılar, Küçükçekmece, Pendik, Ümraniye ve Esenler'dir.
Her biri 500.000 ile 900.000 arasında nüfusa sahip olan bu ilçeler başlı başına büyük şehirler büyüklüğündedir.
İstanbul aynı zamanda önemli bir diaspora şehridir; çok sayıda Ermeni, Rum ve Yahudi topluluk yüzyıllardır bu şehirde yaşamaktadır.
Son yıllarda Suriyeli, Afgan ve diğer yabancı uyruklu sakinlerin sayısında önemli bir artış yaşanmıştır.
Şehrin nüfus yoğunluğu Avrupa'nın en yüksekleri arasında yer almaktadır.
""",

    "ekonomi_ve_is_hayati": """
İstanbul, Türkiye'nin ekonomik başkenti olup ülkenin Gayri Safi Yurt İçi Hasılası'nın yaklaşık yüzde 30'unu üretmektedir.
Şehir, finans, ticaret, sanayi, turizm ve hizmet sektörlerinde Türkiye'nin en büyük merkezidir.
Borsa İstanbul (BIST), Türkiye'nin tek menkul kıymetler borsasıdır ve uluslararası öneme sahiptir.
Büyük Türk bankalarının genel merkezleri İstanbul'da bulunmaktadır.
Levent, Maslak ve Şişli iş bölgeleri Türkiye'nin en değerli ticari gayrimenkul alanlarıdır.
İstanbul Ticaret Odası (İTO), Türkiye'nin en büyük ticaret odasıdır.
Şehirde otomobil, tekstil, gıda, elektronik ve kimya sektörlerinde büyük sanayi kuruluşları faaliyet göstermektedir.
Tuzla, Gebze ve Avcılar gibi ilçeler yoğun sanayi bölgelerine ev sahipliği yapmaktadır.
Turizm İstanbul ekonomisinde kritik bir yer tutmaktadır; her yıl milyonlarca turist şehri ziyaret etmektedir.
İstanbul, Türkiye'ye gelen turistlerin büyük çoğunluğunun ilk durağı konumundadır.
Kentsel dönüşüm projeleri ve gayrimenkul sektörü şehrin ekonomisinde önemli bir pay tutmaktadır.
Teknoloji ve girişimcilik ekosistemi hızla gelişmekte olup pek çok uluslararası şirket İstanbul'a ofis açmaktadır.
""",

    "tarihi_yarimada_ve_surlar": """
Tarihi Yarımada, İstanbul'un en eski ve en önemli bölgesidir. UNESCO Dünya Mirası Listesi'nde yer almaktadır.
Theodosius Surları, MS 5. yüzyılda inşa edilmiş olup dünyada ayakta kalan en iyi korunmuş antik savunma yapılarından biridir.
Surlar, Marmara Denizi'nden Haliç'e kadar yaklaşık 6,5 km boyunca uzanmaktadır.
Tarihi yarımadada Ayasofya, Topkapı Sarayı, Sultan Ahmet Camii (Mavi Cami), Kapalıçarşı ve Mısır Çarşısı gibi eşsiz eserler bulunmaktadır.
Hippodrom Meydanı (Sultanahmet Meydanı), Bizans döneminden kalma antik bir yarış pisti alanıdır; Dikilitaş, Yılanlı Sütun ve Örme Sütun burada yer almaktadır.
Yerebatan Sarnıcı (Basilica Cistern), MS 6. yüzyılda inşa edilmiş devasa bir yeraltı su deposudur.
Çemberlitaş, Beyazıt Meydanı ve Kapalıçarşı çevresindeki tarihi ticaret bölgesi yüzyıllardır faaliyettedir.
Sultanahmet ilçesi adını Sultan 1. Ahmet döneminde yaptırılan Sultanahmet Camii'nden almaktadır.
Tarihi yarımada, eski İstanbul'un surlarla çevrili kesimini oluşturmakta olup tüm Osmanlı ve Bizans döneminin izlerini taşımaktadır.
""",

    "ayasofya": """
Ayasofya, İstanbul'un ve dünyanın en önemli tarihi yapılarından biridir.
MS 537 yılında Bizans İmparatoru I. Justinianus tarafından inşa ettirilmiştir.
İnşaatında dönemin en yetenekli mimarları Anthemios ve İsidoros görev almıştır.
Yaklaşık 1000 yıl boyunca dünyanın en büyük katedrali olan Ayasofya, Hristiyan dünyasının sembolü olmuştur.
1453'te Fatih Sultan Mehmet'in fethinin ardından camiye dönüştürülmüştür.
1934 yılında Atatürk'ün kararıyla müzeye dönüştürülmüş, 2020 yılında yeniden camiye çevrilmiştir.
İçinde ibadet yapılmakla birlikte, turist ziyaretine de açık olan yapı her yıl milyonlarca kişiyi ağırlamaktadır.
Dev kubbesi, İstanbul silüetinin en belirgin simgelerinden biridir; kubbe iç yüksekliği yaklaşık 55 metre, çapı ise 31 metredir.
Yapı, Bizans mozaikleri, mermer sütunlar ve altın yaldızlı süslemeler gibi eşsiz sanat eserleri barındırmaktadır.
Ayasofya, Roma, Bizans, Osmanlı ve Türkiye Cumhuriyeti tarihinin kesişim noktasında duran benzersiz bir eserdir.
""",

    "topkapi_sarayi": """
Topkapı Sarayı, Osmanlı İmparatorluğu'nun idari merkezi olarak yaklaşık 400 yıl kullanılmıştır.
Fatih Sultan Mehmet tarafından 15. yüzyılın ikinci yarısında inşasına başlanmıştır.
Tarihi yarımadanın en uç noktasında, Boğaz, Haliç ve Marmara Denizi'nin kesiştiği stratejik konumda yer almaktadır.
Saray, iç içe geçmiş avlular etrafında düzenlenmiş çeşitli yapılardan oluşmaktadır.
Harem bölümü, padişahların özel yaşam alanlarını barındırmaktadır ve ayrı bir ziyaret turuyla gezilmektedir.
Hazine bölümünde Kaşıkçı Elması, Topkapı Hançeri, Hz. Muhammed'in hırkası gibi değerli eserler sergilenmektedir.
Kutsal Emanetler Dairesi, İslam dünyasının önemli dini objelerini muhafaza etmektedir.
Günümüzde müze olarak hizmet vermekte olup yıllık yaklaşık 3-4 milyon ziyaretçi ağırlamaktadır.
UNESCO Dünya Mirası Listesi'nde yer alan saray, Avrupa'nın en çok ziyaret edilen müzeleri arasındadır.
""",

    "mavi_cami_sultanahmet": """
Sultanahmet Camii, halk arasında Mavi Cami olarak bilinir. Adını iç mekânı süsleyen yaklaşık 20.000 adet çini karolarından almaktadır.
Sultan 1. Ahmet tarafından 1609-1617 yılları arasında mimar Sedefkâr Mehmet Ağa'ya yaptırılmıştır.
Altı minaresiyle İstanbul'da altı minareli nadir camilerden biridir; bu özellik yapıma döneminde büyük tartışmalara neden olmuştur.
Hâlâ aktif bir ibadet yeri olan cami, her gün binlerce turisti ağırlamaktadır.
Namaz vakitlerinde turist ziyaretlerine kısa süreli kapanmaktadır.
Ayasofya'nın tam karşısında yer alması, Sultanahmet Meydanı'na eşsiz bir görünüm kazandırmaktadır.
İç mekânda Bizans etkisi taşıyan mermer sütunlar, zarif kubbeler ve büyük pencereler dikkat çekmektedir.
Cami, İslam mimarisinin en güzel örneklerinden biri olarak kabul edilmektedir.
""",

    "kapalicarsi": """
Kapalıçarşı (Grand Bazaar), dünyanın en büyük ve en eski kapalı çarşılarından biridir.
Fatih Sultan Mehmet döneminde 15. yüzyılda kurulmuş olup yüzyıllar içinde genişlemiştir.
60'tan fazla cadde ve 4.000'in üzerinde dükkândan oluşmaktadır.
Altın, gümüş, mücevher, halı, tekstil, baharat, seramik ve hediyelik eşya satan çok sayıda dükkân bulunmaktadır.
Her yıl yaklaşık 40-90 milyon ziyaretçiyi ağırlayarak dünyanın en çok ziyaret edilen turistik mekânları arasındadır.
Çarşı içindeki bazı esnaf ailesi, kuşaklar boyu aynı alanda ticaret yapmaktadır.
Çarşı, depremler ve yangınlar nedeniyle defalarca yeniden inşa edilmiş; mevcut yapısı büyük ölçüde 18-19. yüzyıla aittir.
Bedesten adı verilen tarihi kapalı ticaret hanları, çarşının en eski bölümlerini oluşturmaktadır.
""",

    "bogaz_ve_uskudar_besiktas": """
İstanbul Boğazı, Karadeniz ile Marmara Denizi'ni birbirine bağlayan ve dünyanın en yoğun kullanılan su yollarından biridir.
Her yıl yaklaşık 45.000-55.000 gemi Boğaz'dan geçmektedir.
Boğaz, Türk Boğazları Sözleşmesi (Montrö Sözleşmesi, 1936) kapsamında yönetilmektedir.
Üsküdar, Asya yakasının tarihi ilçelerinden biridir; Osmanlı döneminden kalma camiler ve tarihi yapılarla doludur.
Kız Kulesi, Üsküdar açıklarında küçük bir adacık üzerinde yükselen ikonik bir yapıdır. Pek çok efsane ve hikâyeye konu olmuştur.
Beşiktaş, Avrupa yakasında Boğaz kıyısındaki canlı ilçelerden biridir. Çarşısı, iskele meydanı ve BJK stadyumuyla tanınır.
Ortaköy, Beşiktaş'a bağlı tarihi ve turistik bir semttir; meşhur kumpir dükkânları ve Ortaköy Camii ile bilinir.
Bebek, varlıklı İstanbullular ve yabancı diplomatların yaşadığı sakin ve yeşil bir Boğaz semtidir.
Emirgan ve Tarabya da Boğaz kıyısında yer alan tercih edilen semtler arasındadır.
Boğaziçi Köprüsü (15 Temmuz Şehitler Köprüsü) ve Fatih Sultan Mehmet Köprüsü, iki kıtayı birbirine bağlayan asma köprülerdir.
""",

    "ulasim": """
İstanbul, kapsamlı bir toplu taşıma ağına sahiptir ancak trafik yoğunluğuyla da ünlüdür.
Metro: İstanbul Metrosu sürekli genişleyen bir ağa sahiptir. M1'den M12'ye kadar uzanan hatlar Avrupa ve Asya yakalarını kapsamaktadır.
Metrobüs: Avrupa yakasında E-5 otoyolu üzerinde işleyen hızlı otobüs sistemidir; günlük yaklaşık 800.000 yolcu taşımaktadır.
Vapur: İDO ve Şehir Hatları vapurları Boğaz, Haliç ve Adalara sefer düzenlemektedir; İstanbul'un ikonik ulaşım araçlarından biridir.
Tramvay: T1 hattı Bağcılar-Kabataş arasında tarihi yarımadayı kat etmektedir. Nostaljik T2 tramvayı ise İstiklal Caddesi'nde çalışmaktadır.
Marmaray: Boğaz'ın altından geçen tünel sistemi Avrupa ve Asya yakalarını hızlı tren ile birbirine bağlamaktadır.
Füniküler (Tünel): 1875 yılında açılan Tünel, İstanbul'un ve dünyanın en eski metro hatlarından biridir; Karaköy ile Beyoğlu arasında çalışmaktadır.
Kabataş Füniküleri: Kabataş iskele ile Taksim Meydanı arasında bağlantı sağlamaktadır.
Deniz taksi ve özel tekne servisleri, kentteki alternatif su ulaşımı seçenekleri arasındadır.
İstanbul Havalimanı (İGA): 2019'da açılan ve dünyanın en büyük havalimanlarından biri olan tesis, Avrupa yakasının kuzeyinde yer almaktadır.
Sabiha Gökçen Havalimanı, Asya yakasında hizmet vermekte olup ağırlıklı olarak düşük maliyetli havayolları tarafından kullanılmaktadır.
Köprüler: E-5 ve TEM otoyollarını birbirine bağlayan üç Boğaz köprüsü —Boğaziçi, FSM ve Yavuz Sultan Selim— günlük milyonlarca araç taşımaktadır.
""",

    "egitim_ve_universiteler": """
İstanbul, Türkiye'nin en fazla üniversiteye sahip şehridir; kamu ve özel toplam 50'yi aşkın yükseköğretim kurumu bulunmaktadır.
İstanbul Üniversitesi, 1453 yılında Fatih Sultan Mehmet tarafından kurulan Sahn-ı Seman Medresesi'ne dayandırılmakta olup Türkiye'nin en köklü üniversitesi kabul edilmektedir.
İstanbul Teknik Üniversitesi (İTÜ), 1773 yılında Osmanlı döneminde kurulan dünyanın en eski teknik üniversitelerinden biridir.
Boğaziçi Üniversitesi, kampüsünü Boğaz kıyısına konumlandırmış ve İngilizce eğitimiyle tanınan prestijli bir devlet üniversitesidir.
Marmara Üniversitesi, Türkiye'nin en büyük üniversitelerinden biridir; birden fazla yerleşkede eğitim vermektedir.
Sabancı Üniversitesi ve Koç Üniversitesi, özel araştırma üniversiteleri arasında uluslararası alanda tanınan iki önemli kurumdur.
Yıldız Teknik Üniversitesi, İstanbul Medipol Üniversitesi, Kadir Has Üniversitesi ve Özyeğin Üniversitesi de İstanbul'un önde gelen üniversiteleri arasındadır.
Şehirde ayrıca pek çok köklü lise, özel okul ve meslek yüksekokulu faaliyet göstermektedir.
Robert Kolej, 1863 yılında kurulan ve Türkiye'nin en prestijli liselerinden biri olarak kabul edilen yatılı bir okuldur.
""",

    "kultur_sanat_muzeler": """
İstanbul, müzeler, sanat galerileri, tiyatrolar ve konser salonlarıyla Türkiye'nin kültür başkentidir.
İstanbul Müzesi (İstanbul Arkeoloji Müzeleri), Eski Şark Eserleri Müzesi ve Çinili Köşk Müzesi olmak üç ayrı yapıdan oluşan bu müze kompleksi dünya çapında önemli eserlere ev sahipliği yapmaktadır.
İstanbul Modern, Karaköy kıyısında yer alan çağdaş sanat müzesidir ve 2023 yılında yenilenen binasıyla kapılarını açmıştır.
Pera Müzesi, Beyoğlu'nda Suna ve İnan Kıraç Vakfı'na ait olup Osmanlı dönemi ve uluslararası eserleri sergilemektedir.
Rahmi M. Koç Müzesi, Haliç kıyısında yer alan ve endüstriyel tarihe adanmış ilgi çekici bir müzedir.
Sakıp Sabancı Müzesi, Emirgan'daki Sabancı ailesinin tarihi yalısında kurulu olup Osmanlı hat sanatı başta olmak üzere zengin koleksiyonlar barındırmaktadır.
Zorlu Performans Sanatları Merkezi (Zorlu PSM) ve Haliç Kongre Merkezi uluslararası düzeyde etkinlikler düzenlemektedir.
İstanbul'da her yıl uluslararası standartlarda pek çok festival gerçekleştirilmektedir: İstanbul Film Festivali, İstanbul Bienali, İstanbul Caz Festivali, İstanbul Tiyatro Festivali bu festivallerin en önemlileri arasındadır.
Türk ve Dünya Müziği Devlet Konservatuvarı ile Devlet Tiyatrosu, şehrin klasik sanat kurumları arasında yer almaktadır.
""",

    "gastronomi_ve_yemek_kulturu": """
İstanbul mutfağı, Türk, Osmanlı, Akdeniz ve Orta Doğu mutfaklarının sentezinden oluşan zengin bir gastronomi geleneğine sahiptir.
Balık ve deniz ürünleri İstanbul mutfağının vazgeçilmezleri arasındadır; Boğaz ve çevre denizlerde avlanan hamsi, istavrit, lüfer, levrek ve çipura başlıca balık türleridir.
Ünlü İstanbul yemekleri arasında simit, balık ekmek, kumpir, midye dolma, kokoreç, tavuk döner, işkembe çorbası ve çeşitli kebap türleri sayılabilir.
Sabah kahvaltısı Türk mutfak kültüründe önemli bir yer tutar; peynir, zeytin, domates, salatalık, menemen ve çay kahvaltı sofralarının olmazsa olmazlarıdır.
Türk çayı sosyal yaşamın merkezinde yer alır; çay evleri ve kahvehaneler hâlâ büyük bir kültürel öneme sahiptir.
Türk kahvesi, 2013 yılında UNESCO İnsanlığın Somut Olmayan Kültürel Mirası Listesi'ne alınmıştır.
İstanbul, son yıllarda dünya genelinde tanınan pek çok restoranıyla uluslararası gastronomi haritasındaki yerini sağlamlaştırmıştır.
Kadıköy Çarşısı ve Balık Pazarı, şehrin en canlı ve otantik yiyecek alışverişi mekânlarından biridir.
Mısır Çarşısı (Baharat Çarşısı) baharatlar, kuruyemişler, lokum ve çeşitli Türk gıda ürünleri için en önemli alışveriş adreslerinden biridir.
""",

    "beyoglu_ve_istiklal": """
Beyoğlu, İstanbul'un en kozmopolit ve hareketli semtlerinden biridir. Tarihsel olarak Pera adıyla bilinmektedir.
İstiklal Caddesi, İstanbul'un en işlek yaya alışveriş caddesidir; her gün 3 milyonu aşkın kişi bu caddeden geçmektedir.
Cadde boyunca tarihi Fransız yapısı binalar, kiliseler, elçilikler, kültür merkezleri, mağazalar ve restoranlar yer almaktadır.
Galata Kulesi, 14. yüzyılda Cenevizliler tarafından inşa edilmiştir; kuleden Boğaz ve şehrin panoramik manzarası seyredilmektedir.
Karaköy, son yıllarda hızla dönüşen ve yaratıcı işletmelerin, galerilerin, kafeler ile restoranların yoğunlaştığı bir bölge hâline gelmiştir.
Cihangir, sanatçılar ve yabancı uyruklu sakinlerin tercih ettiği, İstanbul'un en turizm dostu semtlerinden biridir.
Taksim Meydanı, şehrin ticaret, eğlence ve kültür hayatının kalbi niteliğindedir; pek çok toplumsal etkinliğin de sahne olduğu merkezi bir alandır.
Tunel ve Galata semtleri, kuyumculuk, antika, tasarım mağazaları ve galerileriyle öne çıkan ilgi odağı mekânlardır.
Balık Pazarı (Nevizade Sokağı) ve çevresi, gece hayatının ve meyhane kültürünün canlılığını koruduğu alanlardır.
""",

    "kadikoy_ve_asya_yakasi": """
Kadıköy, Asya yakasının en hareketli ve gelişmiş ilçesi olup kendine özgü bir kültürü ve yaşam tarzı vardır.
Moda, Bağdat Caddesi ve Kadıköy Çarşısı gibi semtler, alışveriş ve gastronomi açısından oldukça zengin seçenekler sunar.
Haydarpaşa Garı, Anadolu'nun fethiyle özdeşleşen ve her Anadolu yolculuğunun çıkış noktası sayılan tarihi tren istasyonudur.
Moda, deniz kıyısındaki parkları ve sakin yapısıyla İstanbul'da yaşam kalitesinin yüksek olduğu semtler arasında gösterilmektedir.
Bağdat Caddesi, Asya yakasının en prestijli alışveriş ve yeme-içme caddesindedir.
Üsküdar, Osmanlı döneminden kalma pek çok cami ve tarihî eseri barındıran, Asya yakasının en eski yerleşim alanlarından biridir.
Çamlıca Tepesi, İstanbul'un en yüksek noktasıdır; hem Avrupa hem de Asya yakasına göz alıcı bir manzara sunmaktadır.
Çamlıca Camii, 2019 yılında açılan Türkiye'nin en büyük camiidir ve Çamlıca Tepesi'nden İstanbul silüetine egemen bir görüntü sergilemektedir.
Bostancı ve Kartal sahil şeridi, İstanbul'da deniz kenarında vakit geçirmek için tercih edilen alanlardandır.
""",

    "dogal_alanlar_ve_parklar": """
İstanbul, büyük kentsel nüfusuna karşın önemli doğal alanlara ve yeşil mekânlara ev sahipliği yapmaktadır.
Belgrad Ormanı, Avrupa yakasında yer alan ve şehrin tarihsel su kaynağı işlevi gören geniş bir ormanlık alandır.
Emirgan Korusu, Boğaz kıyısındaki tarihi bir parkta lalelerle ünlüdür; her yıl nisan ayında düzenlenen Lale Festivali'nin ana mekânıdır.
Yıldız Parkı, tarihi bir saray kompleksi etrafında düzenlenmiş Beşiktaş'taki geniş ve köklü kent parkıdır.
Çamlıca'daki tepeler, şehri çepeçevre kuşatan ormanlarla birlikte İstanbul'un önemli yeşil alanları arasında yer almaktadır.
Florya, Şile ve Kilyos sahilleri deniz tatili için ziyaret edilen kıyı bölgeleridir.
İstanbul Adaları, motorlu araçların yasak olduğu yönetim anlayışıyla doğal ortamını büyük ölçüde korumuştur; bisiklet ve faytonla gezilen bu adalar İstanbullular için doğal bir kaçış noktasıdır.
Hisarüstü ve Polonezköy gibi banliyö semtleri, şehir gürültüsünden uzaklaşmak isteyenlere sakin bir seçenek sunmaktadır.
İstanbul'daki kıyı şeritleri, mesire yerleri ve piknik alanları şehir sakinleri tarafından yoğun biçimde kullanılmaktadır.
""",

    "iklim": """
İstanbul, ılıman iklim koşullarına sahiptir; yazlar sıcak ve nemli, kışlar ise serin ve yağışlı geçmektedir.
Yaz aylarında (Haziran-Ağustos) ortalama sıcaklık 24-28 °C arasında seyreder; nem oranının yüksek olması sıcaklığın daha bunaltıcı hissedilmesine yol açar.
Kış aylarında (Aralık-Şubat) ortalama sıcaklık 4-8 °C arasında değişir; şehirde zaman zaman kar yağışı görülmektedir.
İlkbahar ve sonbahar, İstanbul'u gezmek için en uygun dönemler olarak önerilmektedir.
Şehir, Karadeniz'den esen rüzgârların etkisiyle ani hava değişikliklerine açık bir konumdadır.
Poyraz adı verilen kuzey rüzgârı, özellikle Boğaz'da belirgin biçimde hissedilen kuru ve serin bir rüzgârdır.
Lodos ise güneyden esen ılık ve nemli bir rüzgâr olup zaman zaman şiddetli etkiler gösterebilmektedir.
Yıllık toplam yağış yaklaşık 800 mm olup ağırlıklı olarak kış aylarında düşmektedir.
İklim değişikliğinin etkileriyle birlikte İstanbul'da sıcaklık rekortmen seviyelere çıkmakta ve olağandışı meteorolojik olaylar giderek sık yaşanmaktadır.
""",

    "spor": """
İstanbul, Türkiye'nin spor merkezidir ve özellikle futbol tutkusuyla öne çıkar.
Üç büyük futbol kulübü —Galatasaray, Fenerbahçe ve Beşiktaş— İstanbul'da kurulmuştur ve Türk futbolunun zirvesini temsil etmektedir.
Bu üç kulüp arasındaki rekabet, Türkiye'nin en heyecanlı ve köklü spor rekabetlerinden biridir.
Galatasaray, UEFA Kupası (2000) ve UEFA Süper Kupası'nı (2000) kazanmış olan tek Türk kulübüdür.
İstanbul, 2005 UEFA Şampiyonlar Ligi finaline ev sahipliği yapmıştır; Liverpool ile AC Milan arasında oynanan bu final, futbol tarihine geçen efsanevi bir maç olmuştur.
Türkiye Süper Ligi, Türk Kupası ve Avrupa kupalarındaki maçlar İstanbul'da büyük ilgi görmektedir.
Voleybol, basketbol, güreş ve yüzme İstanbul'da yaygın olarak oynanan diğer spor dallarıdır.
İstanbul Maratonu, dünyanın iki kıtada birden koşulan tek maratonu olma özelliğiyle büyük uluslararası ilgi çekmektedir.
Formula 1 Türkiye Grand Prix'si, İstanbul Park Pisti'nde çeşitli dönemlerde düzenlenmiş; 2020 ve 2021'de pandemi sürecinde tekrar takvime girmiştir.
""",

    "teknoloji_ve_girisimcilik": """
İstanbul, Türkiye'nin teknoloji ve girişimcilik merkezi hâline gelmiştir.
Teknopark İstanbul, İTÜ Teknopark ve Boğaziçi Teknopark gibi teknoloji geliştirme bölgeleri pek çok inovatif şirketi bünyesinde barındırmaktadır.
Türkiye'nin ilk unicorn şirketi Trendyol ve Getir, İstanbul merkezli olup uluslararası alanda ses getirmiştir.
Hepsiburada, Sahibinden ve Gittigidiyor gibi büyük e-ticaret platformlarının genel merkezi İstanbul'dadır.
İstanbul, küresel teknoloji yatırımcılarının ve girişim sermayesi şirketlerinin ilgisini çeken dinamik bir startup ekosistemine sahiptir.
Topluluk çalışma alanları (co-working spaces), hızlandırıcı programlar ve inovasyon merkezleri şehir genelinde hızla çoğalmaktadır.
Nükleer, yenilenebilir enerji ve savunma sanayi alanlarında faaliyet gösteren pek çok teknoloji şirketinin merkezi İstanbul'dadır.
Bilgi Üniversitesi, Sabancı Üniversitesi ve Boğaziçi Üniversitesi teknoloji transferi ve girişimcilik programlarıyla sektörle köprü kurmaktadır.
""",

    "dini_mekanlar_ve_kiliseler": """
İstanbul, çeşitli dinlere ait tarihi ibadet mekânlarına ev sahipliği yapan önemli bir dini çoğulculuk merkezidir.
Eyüp Sultan Camii, Halic'in sonunda yer alan ve derin dini öneme sahip olan ibadet yeridir. İslam aleminde kutsal kabul edilir.
Süleymaniye Camii, Mimar Sinan'ın başyapıtı olarak kabul edilen ve 1557'de tamamlanan muhteşem Osmanlı dönemi eseridir.
Kariye Camii (Chora Kilisesi), İstanbul'un en güzel Bizans mozaiklerine ve fresklerine sahip olup dünyanın benzersiz sanat eserlerinden biri sayılmaktadır.
Ekümenik Patrikane, Fener semtinde yer almakta olup tüm dünya Ortodoks Hristiyanlarının ruhani merkezi kabul edilmektedir.
İstanbul'daki Rum Ortodoks, Ermeni ve Süryani kiliseleri şehrin çok kültürlü dokusunun canlı tanıklarıdır.
Neve Şalom Sinagogu, İstanbul Yahudi topluluğunun en önemli ibadet mekânlarından biridir.
Saint Antoine Kilisesi, İstiklal Caddesi üzerinde yer alan ve İstanbul'un en büyük aktif Katolik kilisesidir.
Rum Ortodoks ve Ermeni cemaatlerine ait onlarca tarihi kilise şehrin çeşitli semtlerine dağılmış durumdadır.
""",

    "ada_ve_marmara": """
İstanbul Adaları (Prens Adaları / Adalar), Marmara Denizi'nde İstanbul'a bağlı 9 adadan oluşmaktadır.
Büyükada (Prinkipo), bu adaların en büyüğü olup 1922'ye kadar Osmanlı dönemi sürgün yeri olarak kullanılmıştır.
Adalarda motorlu taşıt trafiği yasaklıdır; ulaşım fayton, bisiklet ve yürüyüşle sağlanmaktadır.
Adalara ulaşım Kabataş, Bostancı ve diğer iskele noktalarından kalkan vapurlarla gerçekleştirilmektedir.
Heybeliada (Halki), özellikle ekümenik Patrikane ile bağlantılı Ruhban Okulu (şu anda kapalı) ile tanınan ada, dini açıdan tarihi önem taşımaktadır.
Burgazada, Balıkçı Liman Semti ve Hristos Tepesi ile ziyaret edilmesi önerilen sakin bir adadır.
Kınalıada, İstanbul'a en yakın adadır ve günübirlik ziyaretler için oldukça uygundur.
Adalar, özellikle yaz aylarında hem yerli hem yabancı turistlerin gözdesi hâline gelmektedir.
Marmara Denizi'nde yer alan İmralı Adası, cezaevi olarak kullanılmaktadır ve ziyarete kapalıdır.
""",

    "genel_bilgiler": """
İstanbul'un resmi adı İstanbul Büyükşehir Belediyesi'dir.
Şehir kodu 0212 (Avrupa yakası) ve 0216 (Asya yakası) olmak üzere iki ayrı alan koduna sahiptir.
Türkiye Cumhuriyeti'nin resmi başkenti Ankara olmakla birlikte, İstanbul ekonomik, kültürel ve nüfus bakımından ülkenin fiilî merkezi konumundadır.
İstanbul, 2010 yılında Avrupa Kültür Başkenti unvanını taşımıştır.
Şehir, birden fazla defa Avrupa'nın En İyi Seyahat Destinasyonu ödülünü almıştır.
İstanbul'a her yıl 15-20 milyon arasında uluslararası turist gelmektedir; bu rakam onu dünyanın en çok ziyaret edilen şehirleri arasında üst sıralara taşımaktadır.
Şehirde yaklaşık 3.000 cami, onlarca kilise ve çeşitli sinagog bulunmaktadır.
İstanbul, tarihi önemi ve kültürel değerleriyle birçok UNESCO Dünya Mirası Alanı'na ev sahipliği yapmaktadır.
Türk lirası (TRY) şehrin resmi para birimidir; turistik bölgelerde euro ve dolar da yaygın biçimde kabul görmektedir.
Türkçe resmî dildir; turistik alanlarda İngilizce, Almanca ve Arapça da konuşulmaktadır.
"""
}

# Kategori listesi
KATEGORILER = list(ISTANBUL_DOCS.keys())

if __name__ == "__main__":
    print(f"✅ İstanbul veri seti yüklendi!")
    print(f"📂 Toplam kategori sayısı: {len(ISTANBUL_DOCS)}")
    for k in ISTANBUL_DOCS:
        kelime_sayisi = len(ISTANBUL_DOCS[k].split())
        print(f"   - {k}: {kelime_sayisi} kelime")
