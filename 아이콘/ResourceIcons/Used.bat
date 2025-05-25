@echo off
mkdir "Used"
for %%f in (*.dds) do (
    magick "%%f" -resize 48x48 -colorspace Gray "Used\%%~nf.png"
)
