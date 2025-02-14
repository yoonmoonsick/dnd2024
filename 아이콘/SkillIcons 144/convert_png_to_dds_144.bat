@echo off
setlocal enabledelayedexpansion

:: PNG -> DDS 변환 루프
for %%f in (*.png) do (
    echo 변환 중: %%f
    magick convert "%%f" -define dds:compression=BC7 "%%~nf.DDS"
)

echo 변환이 완료되었습니다.

rem 현재 배치 파일이 실행되는 폴더를 원본 폴더로 설정
set "source_folder=%~dp0"

rem 대상 폴더 경로 설정 (여기에 파일을 복사할 폴더를 입력)
set "destination_folder1=D:\BG3\모드툴킷 프로젝트\dnd2024\Mods\DnD2024_897914ef-5c96-053c-44af-0be823f895fe\GUI\Assets\Tooltips\Icons"
set "destination_folder2=D:\BG3\모드툴킷 프로젝트\dnd2024\Mods\DnD2024_897914ef-5c96-053c-44af-0be823f895fe\GUI\Assets\ControllerUIIcons\skills_png"

rem 대상 폴더가 존재하지 않으면 생성
if not exist "!destination_folder!" mkdir "!destination_folder!"

rem DDS 파일 복사 실행
for %%f in ("!source_folder!\*.dds") do (
    copy "%%f" "!destination_folder1!"
    copy "%%f" "!destination_folder2!"
)

echo DDS 파일 복사가 완료되었습니다.
pause


