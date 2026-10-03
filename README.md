# 🛡️ Exosy LogGuard

**Türkçe • Terminal Tabanlı • Güvenlik Log Analiz Aracı**

SSH ve kimlik doğrulama loglarını analiz ederek başarısız giriş denemelerini, başarılı girişleri ve şüpheli IP adreslerini tespit etmek için geliştirilmiş Python tabanlı bir güvenlik aracıdır.

---

## 🔎 Exosy LogGuard Nedir?

**Exosy LogGuard**, siber güvenlik ve Blue Team alanında kendimi geliştirmek amacıyla geliştirdiğim terminal tabanlı bir Python projesidir.

Log dosyalarını analiz ederek tekrarlanan başarısız oturum açma girişlerini tespit eder ve sonuçları anlaşılır bir güvenlik raporu halinde terminal üzerinde gösterir.

> 🎯 Projenin temel amacı log analizi, olay tespiti, Python ve savunma odaklı siber güvenlik konularında pratik yapmaktır.

---

## ✨ Özellikler

- 📂 Log dosyalarını analiz etme
- 🔐 Başarısız SSH girişlerini tespit etme
- ✅ Başarılı SSH girişlerini tespit etme
- 🌐 Kaynak IP adreslerini çıkarma
- 🚨 Tekrarlanan başarısız girişleri tespit etme
- 📊 IP adreslerini deneme sayısına göre sıralama
- ⚠️ Belirlenen eşiği aşan IP adreslerini şüpheli olarak işaretleme
- 🖥️ Düzenli terminal raporu oluşturma
- 🇹🇷 Türkçe terminal arayüzü
- 🐍 Python standart kütüphaneleriyle çalışma

---

## 🚨 Şüpheli IP Tespiti

LogGuard varsayılan olarak aynı IP adresinden **5 veya daha fazla başarısız giriş denemesi** tespit edildiğinde bu adresi şüpheli olarak işaretler.

Bu değer `logguard.py` dosyasındaki:

```python
SUPHELI_ESIK = 5
```

satırından değiştirilebilir.

Örneğin:

```python
SUPHELI_ESIK = 10
```

olarak ayarlanırsa bir IP adresinin şüpheli kabul edilmesi için en az 10 başarısız giriş kaydı gerekir.

---

## 🔍 Algılanan Olaylar

### Başarısız Girişler

LogGuard şu ifadeleri algılayabilir:

```text
Failed password
Authentication failure
Failed login
Invalid user
```

### Başarılı Girişler

```text
Accepted password
Accepted publickey
```

---

## ⚙️ Gereksinimler

Projeyi çalıştırmak için:

- Python 3.x
- Analiz edilecek bir log dosyası

gereklidir.

Proje Python standart kütüphanelerini kullandığından mevcut sürümde ek bir Python paketi yüklemeniz gerekmez.

---

## 🚀 Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/Exosy/Exosy-LogGuard.git
```

Proje klasörüne girin:

```bash
cd Exosy-LogGuard
```

Programı çalıştırın:

```bash
python logguard.py
```

Bazı sistemlerde:

```bash
python3 logguard.py
```

komutunu kullanmanız gerekebilir.

---

## 💻 Kullanım

Program çalıştırıldığında analiz etmek istediğiniz log dosyasının adını girin:

```text
[?] Analiz edilecek log dosyasını girin (örnek: sample.log): sample.log
```

LogGuard dosyayı okuyarak güvenlik olaylarını otomatik olarak analiz eder.

---

## 🧪 Örnek Test

Repository içerisinde bulunan `sample.log` dosyası programı test etmek amacıyla hazırlanmış sentetik SSH kayıtları içerir.

Programı çalıştırın:

```bash
python logguard.py
```

Dosya adı sorulduğunda:

```text
sample.log
```

yazın.

---

## 📊 Örnek Çıktı

```text
╔══════════════════════════════════════════════╗
║              EXOSY LOGGUARD                 ║
║         Güvenlik Log Analiz Aracı           ║
╚══════════════════════════════════════════════╝

SSH/auth loglarındaki giriş olaylarını analiz eder.
Şüpheli IP eşiği: 5 başarısız giriş

==================================================
               ANALİZ SONUÇLARI
==================================================

[+] Log dosyası       : sample.log
[+] Toplam kayıt      : 13
[+] Başarılı giriş    : 2
[!] Başarısız giriş   : 11
[!] Şüpheli IP sayısı : 1

--------------------------------------------------
 EN ÇOK BAŞARISIZ GİRİŞ YAPAN IP ADRESLERİ
--------------------------------------------------

192.0.2.15          6 deneme
198.51.100.22       3 deneme
203.0.113.8         2 deneme

--------------------------------------------------
 ŞÜPHELİ IP ADRESLERİ
--------------------------------------------------

[!] 192.0.2.15       6 başarısız giriş

--------------------------------------------------
 BAŞARILI GİRİŞ KAYNAKLARI
--------------------------------------------------

[+] 192.0.2.50       1 giriş
[+] 192.0.2.60       1 giriş

==================================================
[✓] Log analizi tamamlandı.
==================================================
```

---

## 📁 Proje Yapısı

```text
Exosy-LogGuard/
│
├── logguard.py
├── sample.log
├── README.md
├── .gitignore
└── LICENSE
```

### `logguard.py`

Log analizini gerçekleştiren ana Python programıdır.

### `sample.log`

Programı güvenli şekilde test etmek için hazırlanmış sentetik SSH log kayıtlarını içerir.

### `README.md`

Projenin özelliklerini, kurulumunu, kullanımını ve çalışma mantığını açıklar.

### `.gitignore`

GitHub repository'sine eklenmemesi gereken geçici Python dosyalarını belirler.

### `LICENSE`

Projenin açık kaynak kullanım koşullarını belirtir.

---

## 🧠 Bu Projede Neler Öğreniyorum?

Bu projeyi geliştirirken özellikle şu alanlarda kendimi geliştirmeyi hedefliyorum:

- 🛡️ Blue Team temelleri
- 📊 Güvenlik log analizi
- 🔐 SSH güvenliği
- 🚨 Şüpheli aktivite tespiti
- 🌐 IP tabanlı olay analizi
- 🐍 Python
- 🔎 Regular Expressions (Regex)
- 📂 Dosya işleme
- 🧠 Güvenlik olaylarının yorumlanması

---

## 🗺️ Yol Haritası

### ✅ Tamamlanan Özellikler

- [x] Log dosyası okuma
- [x] Başarısız giriş tespiti
- [x] Başarılı giriş tespiti
- [x] IP adresi çıkarma
- [x] Başarısız girişleri IP bazında sayma
- [x] Şüpheli IP tespiti
- [x] Terminal raporu
- [x] Türkçe terminal çıktısı

### 🚧 Gelecek Özellikler

- [ ] Sonuçları TXT raporuna kaydetme
- [ ] JSON raporu oluşturma
- [ ] CSV çıktısı oluşturma
- [ ] Tarih ve saat bazlı analiz
- [ ] Kullanıcı adı analizi
- [ ] Farklı log formatlarını destekleme
- [ ] Risk seviyesi sistemi
- [ ] Komut satırı argümanları
- [ ] Daha gelişmiş terminal arayüzü
- [ ] İstatistiksel analiz

---

## 🔐 Güvenlik ve Gizlilik

Log dosyaları IP adresleri, kullanıcı adları ve sistem bilgileri gibi hassas veriler içerebilir.

Bu nedenle gerçek sistemlerden alınan logların GitHub gibi herkese açık platformlara yüklenmeden önce hassas bilgilerden temizlenmesi önerilir.

Repository içerisinde bulunan `sample.log` dosyası yalnızca test amacıyla hazırlanmış sentetik veriler kullanır.

---

## ⚠️ Etik Kullanım

Bu proje **eğitim, güvenlik araştırmaları ve savunma amaçlı log analizi** için geliştirilmiştir.

Araç yalnızca erişim yetkinizin bulunduğu loglar ve sistemler üzerinde kullanılmalıdır.

---

## 👨‍💻 Geliştirici

**Exosy**

Siber güvenlik, etik hacking, web güvenliği, OSINT ve Blue Team alanlarında kendimi geliştiriyor ve öğrendiklerimi açık kaynak projeler aracılığıyla paylaşıyorum.

---

## ⭐ Projeyi Destekle

Projeyi faydalı bulduysanız GitHub üzerinden ⭐ bırakabilirsiniz.

**Analiz Et • Tespit Et • Öğren • Savun 🛡️**
