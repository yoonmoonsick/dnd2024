@echo off
mkdir "Missing"
for %%f in (*.dds) do (
    magick "%%f" -resize 48x48 -colorspace Gray -fill red -colorize 50 "Missing\%%~nf.png"
)
