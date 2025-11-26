# 🌌 M.S.E.P. (Midnight Singularity Extraction Program) v0.2 (REDUX)

> **Gelişmiş Otonom OSINT ve Dijital İstihbarat Platformu**

M.S.E.P., "God Mode" protokolü ile çalışan, yapay zeka destekli (Gemini 3.0 Pro) tam otonom bir siber istihbarat aracıdır. Sıradan bir arama motorunun ötesine geçerek; yüzey web, deep web (Tor), forumlar, sosyal medya ve görsel veriler üzerinde derinlemesine analiz yapar, verileri çapraz sorgular ve hedef hakkında kapsamlı bir dijital profil (Dossier) oluşturur.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![AI Core](https://img.shields.io/badge/AI-Gemini%203%20Pro-purple)
![Network](https://img.shields.io/badge/network-Tor%20%26%20Clearweb-red)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🚀 Temel Yetenekler ve Modüller

Sistem, **Merkezi Sinir Sistemi (Core)** ve **Operasyonel Birimler (Black Ops)** olarak iki ana katmanda çalışır.

### 🧠 Core Intelligence (Çekirdek Zeka)

| Modül | Açıklama |
|-------|----------|
| **🧠 Mind Flayer** | Metin ve veri yığınlarını analiz ederek hedefin psikolojik profilini (motivasyonlar, zaaflar, kişilik özellikleri) çıkarır. |
| **👁️ Void Gaze** | **Sherlock Protokolü** ile 15+ platformda (Github, Twitter, Instagram vb.) kullanıcı adı taraması yapar. Google ve Forumlar üzerinde **AI Query Expansion** (Yapay Zeka Destekli Dork Üretimi) ile hibrit arama gerçekleştirir. |
| **🕸️ Constellation** | Toplanan tüm veriler (kişiler, URL'ler, konumlar) arasındaki bağlantıları `NetworkX` ile analiz eder ve ilişki haritası (Graph) oluşturur. |
| **📝 Black Box** | Operasyon sonunda elde edilen tüm ham veriyi işleyerek profesyonel, Markdown formatında bir istihbarat raporu (Dossier) yazar. |
| **⚖️ Inquisitor** | Profildeki eksik bilgileri (Gap Analysis) tespit eder ve operatörü yönlendirerek araştırmanın derinleşmesini sağlar. |

### 🕵️ Black Ops (İleri Düzey Operasyonlar)

| Modül | Açıklama |
|-------|----------|
| **👻 Ghost Walker** | `Playwright` kullanarak JavaScript ağırlıklı dinamik siteleri (Instagram, Twitter) bot korumalarını atlatarak ziyaret eder ve kanıt niteliğinde **tam sayfa ekran görüntüsü** alır. |
| **🧅 Deep Dive** | Yerel **Tor Servisi** (SOCKS5 9050) üzerinden trafiği anonimleştirir ve `.onion` uzantılı Dark Web sitelerinde (Ahmia üzerinden) arama yapar. |
| **🧬 Visual Cortex** | `DeepFace` kütüphanesini kullanarak fotoğraflardaki yüzleri tespit eder; **Yaş, Cinsiyet, Irk ve Duygu** analizi yapar (Biyometrik Tarama). |
| **🕸️ Web Walker** | **ZenRows Premium Scraper** entegrasyonu ile Cloudflare/Captcha korumalı siteleri ve forumları deler. Wayback Machine üzerinden silinmiş içerikleri bulur, PDF dosyalarını okur ve resimlerin **EXIF (GPS)** verilerini analiz ederek konum tespiti yapar. |

---

## 📂 Proje Yapısı

```
msep/
├── cli.py                 # Ana giriş noktası ve CLI arayüzü
├── requirements.txt       # Python bağımlılıkları
├── intel/                 # Toplanan verilerin depolandığı alan
│   └── screenshots/       # Ghost Walker ekran görüntüleri
├── src/
│   ├── mind_flayer.py     # Psikolojik analiz motoru
│   ├── void_gaze.py       # Arama ve keşif motoru (Google/Forumlar)
│   ├── ghost_walker.py    # Tarayıcı otomasyonu (Playwright)
│   ├── deep_dive.py       # Tor/Onion ağ geçidi
│   ├── visual_cortex.py   # Yüz tanıma ve biyometri
│   ├── web_walker.py      # Web kazıma (ZenRows), EXIF ve Arşiv analizi
│   ├── constellation.py   # Ağ haritalama (Graph)
│   ├── black_box.py       # Raporlama sistemi
│   ├── nexus.py           # Karar mekanizması
│   └── config.py          # Ayarlar
└── .env                   # API anahtarları (Gizli)
```

---

## 🛠️ Kurulum ve Hazırlık

### 1. Sistem Gereksinimleri
*   Python 3.10+
*   **Tor Browser** (Deep Dive modülü için arka planda açık olmalı veya `tor` servisi çalışmalı)
*   Google Chrome (Playwright için)

### 2. Kurulum
Repoyu klonlayın ve gerekli paketleri yükleyin:

```bash
git clone https://github.com/kynuxdev/MSEP.git
cd msep
pip install -r requirements.txt
```

Tarayıcı motorlarını yükleyin:
```bash
playwright install
```

### 3. Konfigürasyon (.env)
Ana dizinde `.env` dosyası oluşturun ve API anahtarlarınızı girin:

```env
# Google AI Studio (Gemini) API Key
GEMINI_API_KEY=AIzaSy...

# Google Custom Search API Key
GOOGLE_API_KEY=AIzaSy...

# Google Programmable Search Engine ID (Genel Web)
SEARCH_ENGINE_ID=0123456789...

# Google Programmable Search Engine ID (Görsel Arama - Opsiyonel)
SEARCH_ENGINE_ID_IMAGE=0123456789...

# ZenRows/ScraperAPI Key (Premium Scraping için - Opsiyonel ama Önerilir)
SCRAPING_API_KEY=...
```

---

## 💻 Kullanım

Aracı başlatmak için terminalde:

```bash
python cli.py
```

Sistem açıldığında **M.S.E.P.** terminal arayüzü sizi karşılar. Yapay zeka ajanına doğal dilde emirler verebilirsiniz:

> **Örnek Komutlar:**
> *   *"Mustafa Yılmaz ismini tüm sosyal ağlarda ve dark web'de araştır."*
> *   *"Konsol Oyun hakkında forumlarda (Reddit, Technopat) ne konuşuluyor?"*
> *   *"Şu fotoğrafı analiz et: https://ornek.com/foto.jpg"*
> *   *"https://supheli-site.com adresinin ekran görüntüsünü al ve arşiv kayıtlarına bak."*

### Otonom Protokoller

Ajan, verdiğiniz emri analiz eder ve aşağıdaki araçları zincirleme olarak kullanır:

*   `[SEARCH: "query"]` -> Yüzey araması başlatır.
*   `[FORUM_SCAN: "query"]` -> Forumlarda derinlemesine tarama yapar.
*   `[DEEP_SEARCH: "query"]` -> Tor ağına geçer.
*   `[GHOST_SCAN: url]` -> Siteye gidip fotoğraf çeker.
*   `[BIOMETRIC_SCAN: url]` -> Yüz analizi yapar.
*   `[GAP_ANALYSIS]` -> Eksik bilgileri kontrol eder.
*   `[REPORT]` -> `final_dossier.md` dosyasını oluşturur.

---

## ⚠️ Yasal Uyarı

**DİKKAT:** Bu yazılım (M.S.E.P.), yalnızca **eğitim, araştırma ve yasal güvenlik testleri (Authorized OSINT)** amacıyla geliştirilmiştir.
*   Başkalarının gizliliğini ihlal etmek,
*   İzin alınmadan kişisel veri toplamak,
*   Yasa dışı amaçlarla (Doxing, Cyberstalking vb.) kullanmak,

yerel ve uluslararası yasalara göre suç teşkil edebilir. Geliştiriciler, bu aracın kötüye kullanımından doğacak hiçbir sorumluluğu kabul etmez. **Tüm sorumluluk son kullanıcıya aittir.**

---
*v0.2 (REDUX) - Midnight Singularity Extraction Program*
