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

LogGuard varsayılan olarak aynı IP adresinden **5 veya daha fazla başarısız giriş denemesi** tespit ettiğinde bu adresi şüpheli olarak işaretler.

Bu değer `logguard.py` içerisinde bulunan:

```python
SUPHELI_ESIK = 5
