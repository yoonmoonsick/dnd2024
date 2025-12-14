@echo off
setlocal EnableDelayedExpansion

REM 출력 폴더 생성
if not exist "1_Tooltip_380" mkdir "1_Tooltip_380"
if not exist "2_Controller_144" mkdir "2_Controller_144"
if not exist "4_Readme_48" mkdir "4_Readme_48"

REM 현재 폴더의 모든 PNG 처리
for %%F in (*.png) do (
    set "filename=%%~nF"
    set "fullpath=%%~fF"

    REM 작업 1: 380x380
    magick "!fullpath!" -resize 380x380 "1_Tooltip_380\!filename!.png"

    REM 작업 2: 144x144
    magick "!fullpath!" -resize 144x144 "2_Controller_144\!filename!.png"

    REM 작업 4: 48x48
    magick "!fullpath!" -resize 48x48 "4_Readme_48\!filename!.png"
)

endlocal
