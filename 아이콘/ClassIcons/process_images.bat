@echo off
setlocal

:: 현재 폴더의 모든 PNG 파일에 대해 반복
for %%f in (*.png) do (

    :: 2. 300x300로 사이즈를 변경하여 같은 포맷으로 "1_ClassIcons_300" 폴더에 저장 (파일 이름 동일)
    magick "%%f" -resize 300x300 "1_ClassIcons_300\%%f"

    :: 3. 300x300로 사이즈를 변경하고 DDS 포맷으로 지정된 폴더에 저장 (파일 이름 동일, 확장명 대문자)
    magick "%%f" -resize 300x300 "..\..\Mods\DnD2024_897914ef-5c96-053c-44af-0be823f895fe\GUI\Assets\ClassIcons\%%~nf.DDS"

    :: 4. 140x140로 사이즈를 변경하여 같은 포맷으로 "2_hotbar_140" 폴더에 저장 (파일 이름 동일)
    magick "%%f" -resize 140x140 "2_hotbar_140\%%f"

    :: 5. 140x140로 사이즈를 변경하고 DDS 포맷으로 지정된 폴더에 저장 (파일 이름 동일, 확장명 대문자)
    magick "%%f" -resize 140x140 "..\..\Mods\DnD2024_897914ef-5c96-053c-44af-0be823f895fe\GUI\Assets\ClassIcons\hotbar\%%~nf.DDS"

    echo.
)

endlocal
pause