@echo off
setlocal enabledelayedexpansion

:: PNG -> DDS 변환 루프
for %%f in (*.png) do (
    echo 변환 중: %%f
    magick convert "%%f" -define dds:compression=BC7 "%%~nf.DDS"
)

echo 변환이 완료되었습니다.
pause
