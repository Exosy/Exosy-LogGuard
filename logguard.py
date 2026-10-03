import re
from collections import Counter
from pathlib import Path

BANNER = r"""
╔══════════════════════════════════════════════╗
║              EXOSY LOGGUARD                 ║
║         Güvenlik Log Analiz Aracı           ║
╚══════════════════════════════════════════════╝
"""

# Bir IP bu sayı kadar veya daha fazla başarısız
# giriş yaptıysa şüpheli olarak işaretlenir.
SUPHELI_ESIK = 5

# IPv4 adreslerini yakalamak için kullanılır.
IP_DESENI = re.compile(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
)


def ip_adresi_bul(satir):
    """Bir log satırındaki ilk IPv4 adresini döndürür."""
    eslesme = IP_DESENI.search(satir)

    if eslesme:
        return eslesme.group(0)

    return None


def basarisiz_giris_mi(satir):
    """
    SSH/auth loglarında sık görülen başarısız giriş
    ifadelerini kontrol eder.
    """
    satir = satir.lower()

    anahtar_kelimeler = [
        "failed password",
        "authentication failure",
        "failed login",
        "invalid user",
    ]

    return any(
        kelime in satir
        for kelime in anahtar_kelimeler
    )


def basarili_giris_mi(satir):
    """Başarılı SSH girişlerini tespit eder."""
    satir = satir.lower()

    return (
        "accepted password" in satir
        or "accepted publickey" in satir
    )


def log_analiz_et(dosya_yolu):
    """Belirtilen log dosyasını analiz eder."""

    yol = Path(dosya_yolu)

    if not yol.exists():
        print("\n[!] Belirtilen dosya bulunamadı.")
        return

    if not yol.is_file():
        print("\n[!] Girilen yol bir dosya değil.")
        return

    try:
        satirlar = yol.read_text(
            encoding="utf-8",
            errors="ignore"
        ).splitlines()

    except OSError as hata:
        print(f"\n[!] Dosya okunamadı: {hata}")
        return

    toplam_kayit = len(satirlar)

    basarisiz_giris = 0
    basarili_giris = 0

    basarisiz_ipler = Counter()
    basarili_ipler = Counter()

    for satir in satirlar:

        if basarisiz_giris_mi(satir):
            basarisiz_giris += 1

            ip = ip_adresi_bul(satir)

            if ip:
                basarisiz_ipler[ip] += 1

        elif basarili_giris_mi(satir):
            basarili_giris += 1

            ip = ip_adresi_bul(satir)

            if ip:
                basarili_ipler[ip] += 1

    supheli_ipler = {
        ip: adet
        for ip, adet in basarisiz_ipler.items()
        if adet >= SUPHELI_ESIK
    }

    rapor_yazdir(
        dosya_yolu,
        toplam_kayit,
        basarisiz_giris,
        basarili_giris,
        basarisiz_ipler,
        basarili_ipler,
        supheli_ipler,
    )


def rapor_yazdir(
    dosya,
    toplam,
    basarisiz,
    basarili,
    basarisiz_ipler,
    basarili_ipler,
    supheli_ipler,
):
    """Analiz sonuçlarını terminalde gösterir."""

    print("\n" + "=" * 50)
    print("               ANALİZ SONUÇLARI")
    print("=" * 50)

    print(f"\n[+] Log dosyası       : {dosya}")
    print(f"[+] Toplam kayıt      : {toplam}")
    print(f"[+] Başarılı giriş    : {basarili}")
    print(f"[!] Başarısız giriş   : {basarisiz}")
    print(f"[!] Şüpheli IP sayısı : {len(supheli_ipler)}")

    print("\n" + "-" * 50)
    print(" EN ÇOK BAŞARISIZ GİRİŞ YAPAN IP ADRESLERİ")
    print("-" * 50)

    if basarisiz_ipler:

        for ip, adet in basarisiz_ipler.most_common(10):
            print(f"{ip:<20} {adet} deneme")

    else:
        print("Başarısız giriş kaydı bulunamadı.")

    print("\n" + "-" * 50)
    print(" ŞÜPHELİ IP ADRESLERİ")
    print("-" * 50)

    if supheli_ipler:

        for ip, adet in sorted(
            supheli_ipler.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            print(
                f"[!] {ip:<16} "
                f"{adet} başarısız giriş"
            )

    else:
        print("[✓] Belirlenen eşiği aşan IP bulunamadı.")

    print("\n" + "-" * 50)
    print(" BAŞARILI GİRİŞ KAYNAKLARI")
    print("-" * 50)

    if basarili_ipler:

        for ip, adet in basarili_ipler.most_common():
            print(f"[+] {ip:<16} {adet} giriş")

    else:
        print("Başarılı giriş kaydı bulunamadı.")

    print("\n" + "=" * 50)
    print("[✓] Log analizi tamamlandı.")
    print("=" * 50)


def main():

    print(BANNER)

    print(
        "SSH/auth loglarındaki giriş olaylarını analiz eder."
    )

    print(
        f"Şüpheli IP eşiği: {SUPHELI_ESIK} "
        "başarısız giriş\n"
    )

    dosya = input(
        "[?] Analiz edilecek log dosyasını girin "
        "(örnek: sample.log): "
    ).strip()

    if not dosya:
        print("[!] Dosya adı boş bırakılamaz.")
        return

    log_analiz_et(dosya)


if __name__ == "__main__":
    main()
