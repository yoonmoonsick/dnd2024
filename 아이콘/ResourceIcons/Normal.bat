@echo off
mkdir "Normal"
for %%f in (*.dds) do (
    magick "%%f" -resize 48x48 "Normal\%%~nf.png"
)
