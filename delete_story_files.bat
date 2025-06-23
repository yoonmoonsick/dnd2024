@echo off
echo Baldur's Gate 3 모드 파일을 삭제합니다...
echo.

set "MOD_PATH=D:\SteamLibrary\steamapps\common\Baldurs Gate 3\Data\Mods\DnD2024_897914ef-5c96-053c-44af-0be823f895fe\Story"

del "%MOD_PATH%\goals.raw"
del "%MOD_PATH%\log.txt"
del "%MOD_PATH%\story.div"
del "%MOD_PATH%\story.div.osi"
del "%MOD_PATH%\story_ac.dat"
del "%MOD_PATH%\story_orphanqueries_found.txt"
del "%MOD_PATH%\story_orphanqueries_ignore.txt"

echo.
echo 파일 삭제가 완료되었습니다.
pause