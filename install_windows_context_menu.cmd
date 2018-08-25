set PYTHON_PATH=
for %%i in ("%~dp0.") do SET "EXEC_PATH=%%~fi"
set EXEC=CiaServer.py

reg add hkcr\.cia /d "3ds.software" /f
reg add "hkcr\3ds.software\shell\Create QR Code\command" /d "\"%PYTHON_PATH%\pythonw.exe\" \"%EXEC_PATH%\%EXEC%\" \"%%1\"" /f
