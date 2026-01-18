@echo off
setlocal enabledelayedexpansion

mkdir "0_Controller_80"
for %%f in (*.dds) do (
    magick "%%f" -resize 80x80 "0_Controller_80\%%~nf.png"
)

mkdir "1_Normal_48"
for %%f in (*.dds) do (
    magick "%%f" -resize 48x48 "1_Normal_48\%%~nf.png"
)

mkdir "2_Highlight_48"
set "source=%cd%"
set "destination=%cd%\2_Highlight_48"

for %%f in (*.dds) do (
    set "filename=%%~nf"
    set "output=!destination!\!filename!.png"

    rem 밝기 25% 증가 + glow 효과 적용
    magick ^
    ^( "%%f" -resize 48x48 -modulate 125,100,100 ^) ^
    ^( -clone 0 -blur 0x16 -evaluate multiply 0.5 ^) ^
    -compose screen -composite "!output!"
)

mkdir "3_Missing_48"
for %%f in (*.dds) do (
    magick "%%f" -resize 48x48 -colorspace Gray -fill red -colorize 50 "3_Missing_48\%%~nf.png"
)

mkdir "4_Used_48"
for %%f in (*.dds) do (
    magick "%%f" -resize 48x48 -colorspace Gray "4_Used_48\%%~nf.png"
)

mkdir "0_Controller_80"
for %%f in (*.png) do (
    magick "%%f" -resize 80x80 "0_Controller_80\%%~nf.png"
)

mkdir "1_Normal_48"
for %%f in (*.png) do (
    magick "%%f" -resize 48x48 "1_Normal_48\%%~nf.png"
)

mkdir "2_Highlight_48"
set "source=%cd%"
set "destination=%cd%\2_Highlight_48"

for %%f in (*.png) do (
    set "filename=%%~nf"
    set "output=!destination!\!filename!.png"

    rem 밝기 25% 증가 + glow 효과 적용
    magick ^
    ^( "%%f" -resize 48x48 -modulate 125,100,100 ^) ^
    ^( -clone 0 -blur 0x16 -evaluate multiply 0.5 ^) ^
    -compose screen -composite "!output!"
)

mkdir "3_Missing_48"
for %%f in (*.png) do (
    magick "%%f" -resize 48x48 -colorspace Gray -fill red -colorize 50 "3_Missing_48\%%~nf.png"
)

mkdir "4_Used_48"
for %%f in (*.png) do (
    magick "%%f" -resize 48x48 -colorspace Gray "4_Used_48\%%~nf.png"
)