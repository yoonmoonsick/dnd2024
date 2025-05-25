@echo off
mkdir "ActionResourcesc\Icons"
for %%f in (*.dds) do (
    magick "%%f" -resize 80x80 "ActionResourcesc\Icons\%%~nf.png"
)
