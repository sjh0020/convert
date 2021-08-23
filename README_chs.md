利用notepad++实现文件批量转换编码格式
python

使用方法
===========
     一、安装Python Script 插件
     1.插件主页：https://github.com/bruderstein/PythonScript
     2.下载PythonScript_Full_1.5.4.0_x64.zip
     3.解压压缩包到C:\Program Files\Notepad++\plugins\PythonScript
    二、新建python脚本
      重启Notepad++
      Choose menu Plugins->Python Script->New script （选择插件>python 脚本>新建脚本）
	  导入Convert to UTF-16 LE BOM.py
	  或把文件移动到C:\Users\*****\AppData\Roaming\Notepad++\plugins\Config\PythonScript\scripts
     三、运行脚本
      重启Notepad++
	  Choose menu Plugins->Python Script->勾选Show Console
	  Choose menu Plugins->Python Script->Script->Convert to UTF-16 LE BOM

注意事项
===========
    1.notepad ++ 必须是在 英文状态下上述 方法才有效
    2.filePathSrc 路径中不能包含中文
    3.python不支持tab 和空格混用 缩进，所以最好是打开notepad++ 的 View–>Show Symbol->勾选Show White Space and TAB
    4.使用前请检查脚本运行的目标目录有对应格式文件
    5.如果要转化为ANSI 就把第11行即【notepad.runMenuCommand("Encoding", "Convert to UTF-16 LE BOM")】中UTF-16 LE BOM替换为ANSI即可，请确保转换的编码格式为muen中Ecoding含Convert的选项 
    6.第9行中【fn[-3:] == '.ks'】指寻找后3个字符匹配路径后缀为.ks
    7.如果你要匹配.cpp ，则应该是fn[-4:]
    8.保存好的脚本文件不能再更改，否则会运行失败
