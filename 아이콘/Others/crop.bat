@echo off
setlocal enabledelayedexpansion

REM ImageMagick convert 명령어 경로 설정 (필요 시 수정)
set IM_CONVERT=magick convert

REM 현재 폴더의 모든 .dds 파일 처리
for %%F in (*.dds) do (
    REM 파일 이름 추출 (확장자 제외)
    set "filename=%%~nF"

    REM 출력 폴더 생성
    mkdir "!filename!"

    REM 이미지 사이즈를 알아내기 위해 identify 사용
    for /f "tokens=1,2 delims=x " %%W in ('magick identify -format "%%w %%h" "%%F"') do (
        set "imgWidth=%%W"
        set "imgHeight=%%H"
    )

    REM 각 파일을 64x64로 자르기
    %IM_CONVERT% "%%F" -crop 64x64 "!filename!\tile_%%d.png"
)

echo 완료되었습니다.
pause
