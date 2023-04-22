$usr = $env:username
# move files
New-Item -Path "C:\Users\$usr\AppData\Roaming\" -Name "BMPConv" -ItemType "directory"
Copy-item "main.py" -destination "C:\Users\$usr\AppData\Roaming\BMPConv"

# create profile
if(-Not (Test-Path $profile)){
    New-Item -Path $profile -Type File -Force
}
# add aliases
Add-Content $profile "`r`n #BMPConv profile, more about project: https://github.com/koszalix/BMPConv"
Add-Content $profile "function _BMPConv{ python C:\Users\$usr\AppData\Roaming\BMPConv\main.py @args}"
Add-Content $profile "Set-Alias -Name BMPConv -Value _BMPConv -Description 'BMPConv script alias https://github.com/koszalix/FileSorter'"

