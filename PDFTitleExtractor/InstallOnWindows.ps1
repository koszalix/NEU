$usr = $env:username
# move files
New-Item -Path "C:\Users\$usr\AppData\Roaming\" -Name "PDFTitleExtractor" -ItemType "directory"
Copy-item "main.py" -destination "C:\Users\$usr\AppData\Roaming\PDFTitleExtractor"

# create profile
if(-Not (Test-Path $profile)){
    New-Item -Path $profile -Type File -Force
}
# add aliases
Add-Content $profile "`r`n #PDFTitleExtractor profile, more about project: https://github.com/koszalix/PDFTitleExtractor"
Add-Content $profile "function _PDFTitleExtractor{ python C:\Users\$usr\AppData\Roaming\PDFTitleExtractor\main.py @args}"
Add-Content $profile "Set-Alias -Name PDFTitleExtractor -Value _PDFTitleExtractor -Description 'PDFTitleExtractor script alias https://github.com/koszalix/FileSorter'"