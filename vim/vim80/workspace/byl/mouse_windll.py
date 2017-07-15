#coding=utf-8
#---------------
#模拟鼠标
#提供和C语言兼容的数据类型，可以很方便地调用C DLL中的函数
#
#---------------
from ctypes import * 
import win32gui
import win32con
import win32api
import time

"获取鼠标位置"
win32gui.GetCursorPos()

"设置鼠标位置"
windll.user32.SetCursorPos(100, 100)

pos = [200,300]
"鼠标左键点击"
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0], pos[1])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0], pos[1])


#鼠标右键
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, pos[0], pos[1])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, pos[0], pos[1])
