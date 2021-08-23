# Convert
This is a script for Notepad++ which can batch convert you file encoding.

[Engish](https://github.com/sjh0020/convert/blob/master/README.md)  |  [中文](https://github.com/sjh0020/convert/blob/master/README_chs.md)

## Install plugin

Install a plugin [PythonScript](https://github.com/bruderstein/PythonScript/releases/latest)

Download the x86(PythonScript_Full_x.x.x.x.zip) or x64(PythonScript_Full_x.x.x.x_x64.zip)

Exctarct the zip to you notepad++ install path/plugin/PythonScript(default:C:\Program Files\Notepad++\plugins\PythonScript)

## Load the script

Open notepad++ and choose Menu of Plugins -> Python Script -> New Script,then enter a easy memory file name

Copy the content of Convert to _UTF-16 LE BOM.py_ in your new file
Or copy _UTF-16 LE BOM.py_ to C:\Users\username\AppData\Roaming\Notepad++\plugins\config\PythonScript\scripts and rename

Edit your script work path on line 5 such as 
> filePathSrc="D:\\doc\\1"

Edit yourself want to convert file extension name on line 8 such as
>           if fn[-3:] == '.ks':
If you want to convert two or more file extension in once,you can like
>           if fn[-3:] == '.ks' or fn[-5:] == '.html':

Edit your expection command on line 10 such as
>              notepad.runMenuCommand("Encoding", "Convert to UTF-8")
attention your command should from the notepad++ Menu

save your python script and restart notepad++

Show the console : Menu Plugins -> Python Script ->Menu Plugins -> Python Script -> Show Console

use the script : Menu Plugins -> Python Script -> Scripts -> choose youself script
## attention

1. set your notepad++ language in English : Menu Settings -> Preferences -> General -> localization -> English
2. filePathSrc(your script work path) must in English,and exist folder and files
_you must ensurence you filePath and file name all in English_
3. Python can't support both use of Tab and Space.So you can open the setting to distinguish Tab/Space : Menu View -> Show Symbol -> Show White Space ang TAB
