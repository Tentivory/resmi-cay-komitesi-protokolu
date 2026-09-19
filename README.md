# Resmî Çay Komitesi Protokolü

> **UYARI:** Bu yazılım bir şaka değildir. Şaka gibi durması, şaka olduğu anlamına gelmez. Şaka olsaydı zaten tutanak tutulmazdı.

## Misyon

Bu proje, çay demleme sürecini bireysel keyiften çıkarıp **kurul kararına** bağlar.  
Bardak, demlik, şeker ve bekleyen insan aynı anda mutlu edilemez. Komite bunu resmi olarak kabul eder, sonra yine de oy kullanır.

## Kuruluş Gerekçesi

Tarih boyunca nice medeniyet çay yüzünden dağılmamıştır.  
Bu yazılım o geleneği bozmamak için yazıldı.

## Kurulum

```bash
python3 komite.py
```

Python 3 yeter. Bağımlılık yok. Bütçe yok. Sadece irade var.

## Kullanım

Program sizi şu konularda oylamaya zorlar:

1. Demlik tipi (ince belli / koca göbek / kimse sormasın)
2. Bekleme süresi (dakika değil, **tutanak dakikası**)
3. Şeker politikası (0 / 1 / 2 / "konuşmayalım")

Sonuç olarak size bir **Resmî Demleme Kararı** basar.  
Karara itiraz etmek için issue açabilirsiniz. Issue'lar da çay gibi demlenir: uzun sürer, sonu belirsizdir.

## Mimari

- `komite.py` — tek dosyalı devlet
- rastgele sayı üreteci — halk iradesi simülasyonu
- `DAMGA.txt` — mühür

## Sık Sorulan Sorular

**Bu gerçekten çalışıyor mu?**  
Evet. Çalışması, işe yaramasından farklıdır.

**Neden Türkçe?**  
Çünkü çay Türkçe konuşur.

**Copilot bu kodu beğendi mi?**  
Copilot'a sorduk. "LGTM ama demlik çok büyük" dedi. Tutanaklara geçti.

## Lisans

Herkes içer. Bazı bardaklar daha sıcak gelir. Bu bir lisans maddesi değildir, gözlemidir.

---
