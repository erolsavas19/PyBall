# PyBall

Klasik Breakout tarzı, Python ile geliştirilmiş tam ekran arcade oyunu.

---

## Özellikler

- 10 bölüm, artan zorluk seviyesi
- 12 farklı güçlendirme (power-up)
- Yıldız animasyonlu arka plan
- Skor tablosu (ilk 10)
- Fare ve klavye desteği
- Ayarlanabilir ses efektleri, müzik ve FPS
- Ağ üzerinde çok kullanıcılı çalışma desteği

---

## Gereksinimler

- Python 3.10+
- pygame

```
pip install pygame
```

---

## Çalıştırma

```
python pyBall.py
```

---

## Kontroller

| Tuş / Hareket | İşlev |
|---|---|
| **Fare** / **← →** | Paddle'ı hareket ettir |
| **Space** / **Sol tık** | Topu fırlat |
| **M** | Fare ↔ Klavye geçişi |
| **F1** | Yardım ekranı |
| **ESC** | Menüye dön / Çıkış |

---

## Güçlendirmeler

| Sembol | Renk | Etki (30 sn) |
|---|---|---|
| **B** | Yeşil | Paddle büyür |
| **K** | Mavi | Paddle küçülür |
| **X** | Mor | Hayalet top — blokları delerek geçer |
| **C** | Kırmızı | +1 Can (maks. 5) |
| **O** | Turuncu | −1 Can |
| **H** | Sarı | Top hızlanır |
| **M** | Camgöbeği | Top küçülür ve hızlanır |
| **Y** | Pembe | Top sayısı 3'e çıkar |
| **Z** | Açık Yeşil | Top büyür, 5 tuğla kırar, duvar hasarı verir |
| **D** | Mavi | Altta bariyer oluşur |
| **T** | Altın | Yapışkan top — paddle'a yapışır |
| **A** | Turuncu-Kırmızı | Ateş modu — Space / tık ile mermi fırlatır |

---

## Özel Bloklar

- **Çarpılı Siyah Bloklar** — Kırılamaz, 4. bölümden itibaren çıkar; sayısı ilerledikçe artar.

---

## Zorluk Seviyeleri

| Bölüm | Hız | Siyah Blok |
|---|---|---|
| 1 – 3 | Normal | Yok |
| 4 – 7 | Orta | 1–2 adet |
| 8 – 10 | Yüksek | 3 adet |

---

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `pyBall.py` | Oyun kaynak kodu |
| `pyBall.ico` | Uygulama simgesi |
| `highscores.json` | Paylaşımlı skor tablosu |
| `%APPDATA%\PyBall\settings.json` | Kullanıcıya özel ayarlar |
| `derle.bat` | PyInstaller ile exe derleme aracı |

---

## Windows Defender Uyarısı

`pyBall.exe` dijital imza içermediğinden Windows Defender ilk çalıştırmada engelleyebilir.

**Çözüm:**
1. **Windows Güvenliği** → Virüs ve tehdit koruması
2. **Virüs ve tehdit koruması ayarları** → Dışlamalar
3. **Dışlama ekle** → Klasör → `pyBall.exe`'nin bulunduğu klasörü seçin

Veya Microsoft'a yanlış pozitif bildirimi yapabilirsiniz:
https://www.microsoft.com/en-us/wdsi/filesubmission

---

## Derleme (EXE)

`derle.bat` dosyasını çalıştırın. Derlenen dosya `dist\pyBall.exe` konumuna çıkar.

UPX ile daha küçük boyut için `upx.exe`'yi `C:\upx\` klasörüne koyun — `derle.bat` otomatik algılar.

---

## Geliştirici

**FreewareTR.com** — Ücretsiz yazılım arşivi  
**youtube.com/CaprazBilgi** — Yazılım ve teknoloji içerikleri
