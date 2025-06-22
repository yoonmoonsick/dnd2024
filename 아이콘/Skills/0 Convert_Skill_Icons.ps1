$files = Get-ChildItem -Filter *.png

New-Item -ItemType Directory -Force -Path "1_Tooltip_380" | Out-Null
New-Item -ItemType Directory -Force -Path "2_Controller_144" | Out-Null
New-Item -ItemType Directory -Force -Path "3_Atlas_64" | Out-Null

foreach ($file in $files) {
    $filename = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
    $fullPath = $file.FullName

    # 작업 1: 380x380 리사이즈 → PNG 저장
    & cmd /c "magick `"$fullPath`" -resize 380x380 `1_Tooltip_380\$filename.png`"
    # 작업 1: PNG를 DDS로 변환 (BC7 압축)
    & cmd /c "magick `1_Tooltip_380\$filename.png` -define dds:compression=BC7 `1_Tooltip_380\$filename.DDS`"

    # 작업 2: 144x144 리사이즈 → PNG 저장
    & cmd /c "magick `"$fullPath`" -resize 144x144 `2_Controller_144\$filename.png`"
    # 작업 2: PNG를 DDS로 변환 (BC7 압축)
    & cmd /c "magick `2_Controller_144\$filename.png` -define dds:compression=BC7 `2_Controller_144\$filename.DDS`"

    # 작업 3: spell_bg.DDS 합성 후 PNG 저장
    & cmd /c "magick `spell_bg.DDS` -resize 144x144 ( `"$fullPath`" -resize 144x144 ) -gravity center -composite `3_Atlas_64\$filename.png`"
    # 작업 3: PNG를 DDS로 변환 (BC7 압축)
    & cmd /c "magick `3_Atlas_64\$filename.png` -define dds:compression=BC7 `3_Atlas_64\$filename.DDS`"
}
