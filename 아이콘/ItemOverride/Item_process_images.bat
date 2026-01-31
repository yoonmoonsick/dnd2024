@echo off
setlocal

:: 현재 폴더의 모든 PNG 파일에 대해 반복
for %%f in (*.png) do (

    :: 1. DDS 포맷으로 지정된 폴더에 저장 (파일 이름 동일, 확장명 대문자)
    magick "%%f" "..\..\Mods\DnD2024_897914ef-5c96-053c-44af-0be823f895fe\GUI\Assets\Tooltips\ItemIcons\%%~nf.DDS"

    :: 2. DDS 포맷으로 지정된 폴더에 저장 (파일 이름 동일, 확장명 대문자)
    magick "%%f" "..\..\Mods\DnD2024_897914ef-5c96-053c-44af-0be823f895fe\GUI\Assets\ControllerUIIcons\items_png\%%~nf.DDS"

    echo.
)

endlocal
pause