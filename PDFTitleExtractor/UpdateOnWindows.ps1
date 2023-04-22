$usr = $env:username
Remove-Item "C:\Users\$usr\AppData\Roaming\PDFTitleExtractor\main.py"
Copy-item "main.py" -destination "C:\Users\$usr\AppData\Roaming\PDFTitleExtractor"