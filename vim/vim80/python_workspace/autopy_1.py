# coding=utf-8
import autopy

autopy.mouse.move(100, 100) 

#autopy.mouse.smooth_move(400, 400) 

#vim 里面lua 是1，python 2.7 也是1

'''
Traceback (most recent call last):
  File "autopy_1.py", line 4, in <module>
    import autopy
  File "D:\python_workspace\autopy.py", line 2, in <module>
AttributeError: 'module' object has no attribute 'mouse'
shell returned 1
Hit any key to close this window...
问题解决了
目录下有个autopy.pyc文件，删除就好了。
pyc文件是py文件由编译器生成的字节码，所以不要命名和内置库同名的py文件，避免冲突。

'''

