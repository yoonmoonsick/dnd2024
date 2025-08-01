$files = Get-ChildItem -Filter *.png

New-Item -ItemType Directory -Force -Path "1_Tooltip_380" | Out-Null
New-Item -ItemType Directory -Force -Path "2_Controller_144" | Out-Null
New-Item -ItemType Directory -Force -Path "4_Readme_48" | Out-Null

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

    # 작업 4: 48x48 리사이즈 → PNG 저장
    & cmd /c "magick `"$fullPath`" -resize 48x48 `4_Readme_48\$filename.png`"
    # 작업 4: PNG를 DDS로 변환 (BC7 압축)
    & cmd /c "magick `4_Readme_48\$filename.png` -define dds:compression=BC7 `4_Readme_48\$filename.DDS`"

}
