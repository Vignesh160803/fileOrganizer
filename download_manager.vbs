Set WshShell = CreateObject("WScript.Shell")
Do
    WshShell.Run "pythonw.exe absolute path of the application .py file", 0, True
    WScript.Sleep 5000  
Loop
Set WshShell = Nothing
