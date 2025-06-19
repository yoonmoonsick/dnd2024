@echo off
setlocal enabledelayedexpansion

rem 변환할 폴더 리스트
set folders=1_Tooltip_380 2_Controller_144 3_Atalas_64

for %%F in (%folders%) do (
    echo Processing folder: %%F
    pushd %%F
    for %%I in (*.png) do (
        echo Converting %%I to DDS...
        magick "%%I" "%%~nI.DDS"
    )
    popd
)

echo Conversion completed.
pause
