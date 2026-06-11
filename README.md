# PyBall

Classic Breakout-style fullscreen arcade game developed with Python.

---

## Features

- 10 levels with increasing difficulty
- 12 different power-ups
- Star-animated background
- High score table (top 10)
- Mouse and keyboard support
- Adjustable sound effects, music, and FPS
- Multiplayer support over network

---

## Requirements

- Python 3.10+
- pygame

```
pip install pygame
```

---

## Run

```
python pyBall.py
```

---

## Controls

| Key / Action | Function |
|---|---|
| **Mouse** / **← →** | Move paddle |
| **Space** / **Left click** | Launch ball |
| **M** | Toggle mouse ↔ keyboard |
| **F1** | Help screen |
| **ESC** | Return to menu / Exit |

---

## Power-Ups

| Symbol | Color | Effect (30 sec) |
|---|---|---|
| **B** | Green | Paddle grows |
| **K** | Blue | Paddle shrinks |
| **X** | Purple | Ghost ball — passes through blocks |
| **C** | Red | +1 Life (max 5) |
| **O** | Orange | −1 Life |
| **H** | Yellow | Ball speeds up |
| **M** | Cyan | Ball shrinks and speeds up |
| **Y** | Pink | Ball count increases to 3 |
| **Z** | Light Green | Ball grows, breaks 5 bricks, damages walls |
| **D** | Blue | Barrier forms at the bottom |
| **T** | Gold | Sticky ball — sticks to paddle |
| **A** | Orange-Red | Fire mode — launch bullets with Space / click |

---

## Special Blocks

- **Striped Black Blocks** — Indestructible, appear from level 4 onward; count increases as levels progress.

---

## Difficulty Levels

| Level | Speed | Black Block |
|---|---|---|
| 1 – 3 | Normal | None |
| 4 – 7 | Medium | 1–2 blocks |
| 8 – 10 | High | 3 blocks |

---

## Files

| File | Description |
|---|---|
| `pyBall.py` | Game source code |
| `pyBall.ico` | Application icon |
| `highscores.json` | Shared high score table |
| `%APPDATA%\PyBall\settings.json` | User-specific settings |
| `derle.bat` | PyInstaller exe build tool |

---

## Windows Defender Warning

Since `pyBall.exe` does not contain a digital signature, Windows Defender may block it on first run.

**Solution:**
1. **Windows Security** → Virus & threat protection
2. **Virus & threat protection settings** → Exclusions
3. **Add an exclusion** → Folder → Select the folder containing `pyBall.exe`

Or you can submit a false positive report to Microsoft:
https://www.microsoft.com/en-us/wdsi/filesubmission

---

## Build (EXE)

Run `derle.bat`. The compiled file is output to `dist\pyBall.exe`.

For smaller size with UPX, place `upx.exe` in `C:\upx\` — `derle.bat` detects it automatically.

---

## Developer

**FreewareTR.com** — Free software archive  
**youtube.com/CaprazBilgi** — Software and technology content

---
---

# PyBall (Türkçe)

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
