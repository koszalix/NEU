$usr = $env:username
# move files
New-Item -Path "C:\Users\$usr\AppData\Roaming\" -Name "FileSorter" -ItemType "directory"
Copy-item "main.py" -destination "C:\Users\$usr\AppData\Roaming\FileSorter"

# create profile
if(-Not (Test-Path $profile)){
    New-Item -Path $profile -Type File -Force
}
# add aliases
Add-Content $profile "# File sorter aliases, more about project: https://github.com/koszalix/FileSorter"
Add-Content $profile "function _fileSorter{ python C:\Users\pawel\AppData\Roaming\FileSorter\main.py @args}"
Add-Content $profile "Set-Alias -Name FileSorter -Value _fileSorter -Description 'File sorter script alias https://github.com/koszalix/FileSorter'"

