@echo off
echo ============================================
echo   PyBall - Nuitka Derleme Araci
echo ============================================
echo.

:: Nuitka kurulu mu?
python -m nuitka --version >nul 2>&1
if errorlevel 1 (
    echo Nuitka bulunamadi. Kuruluyor...
    pip install nuitka
    if errorlevel 1 (
        echo HATA: Nuitka kurulanamadi!
        pause
        exit /b 1
    )
)

:: Eski derleme kalıntilarini temizle
if exist "pyBall.dist"  rmdir /s /q pyBall.dist
if exist "pyBall.build" rmdir /s /q pyBall.build

echo Derleniyor... (ilk derlemede 5-10 dakika surebilir)
echo.

python -m nuitka ^
    --onefile ^
    --windows-disable-console ^
    --windows-icon-from-ico=pyBall.ico ^
    --output-filename=pyBall.exe ^
    pyBall.py

if errorlevel 1 (
    echo.
    echo HATA: Derleme basarisiz!
    pause
    exit /b 1
)

:: Build klasorunu temizle
if exist "pyBall.build" rmdir /s /q pyBall.build

echo.
echo ============================================
echo   Tamamlandi!  -^>  pyBall.exe
echo ============================================
echo.
pause
