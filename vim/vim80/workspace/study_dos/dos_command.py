dir /?

只显示目录
dir /a:d

ren 或 rename[编辑]
重命名文件或者一个子目录
语法
RENAME [drive:][path]filename1 filename2 例如：rename d:\soft\setup.exe setup123.exe REN [drive:][path]filename1 filename2

del 或 erase[编辑]
删除一个或者多个文件
语法
ERASE [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names
DEL [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names
参数说明：
/F 强制删除只读文件。
/S 从所有子目录删除指定文件。
/Q 安静模式。删除时，不要求确认。
/A 根据属性选择要删除的文件。
示例：
del /f /s /q /a c:\*.bak
就是删除所有在 c 槽的 *.bak 档
假如是一个目录的话就
del /q c:\folder\*.bak
