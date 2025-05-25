@echo off
setlocal enabledelayedexpansion

rem 원본 폴더: 현재 디렉토리
set "source=%cd%"
set "destination=%cd%\Highlight"

rem 결과 폴더 생성
if not exist "%destination%" (
    mkdir "%destination%"
)

rem 모든 DDS 파일 반복 처리
for %%f in (*.dds) do (
    set "filename=%%~nf"
    set "output=%destination%\!filename!.png"

    rem 밝기 25% 증가 + glow 효과 적용
    magick ^
    ^( "%%f" -resize 48x48 -modulate 125,100,100 ^) ^
    ^( -clone 0 -blur 0x16 -evaluate multiply 0.5 ^) ^
    -compose screen -composite ^
    "!output!"
)

echo 작업 완료: Highlight 폴더에 저장됨.
