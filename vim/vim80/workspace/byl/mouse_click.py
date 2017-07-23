# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
mouse click

'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"
import win32con
import win32api 
import ctypes,time
from ctypes import wintypes
from ctypes import *
from win32api import GetSystemMetrics

def fenBianlv():
    "根据屏幕分辨率计算偏移系数px和py"
    "取得屏幕分辨率"
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    "计算相对默认1680,  1050的偏移量"
    w = 1680.0
    h = 1050.0
    px = w/width
    py = h/height
    pxy = list(range(2)) 
    pxy[0] = px
    pxy[1] = py
    return pxy 
def click(x,y):
    "鼠标移动指定位置,左键点击一下"
    fbl = []
    fbl = fenBianlv()
    x1 = int(x*fbl[0]) 
    y1 = int(y*fbl[1]) 
    windll.user32.SetCursorPos(x1, y1)
    print 'mouse move to {}, {}'.format(x1,y1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1)
#click(120,150)

def shooting():
    "定点循环攻击"
    x = 1287 
    y = 637 
    x1 = int(x*fenBianlv()[0])
    y1 = int(y*fenBianlv()[1])
    #autopy.mouse.move(x, y) 
    while True:
        windll.user32.SetCursorPos(x1, y1)
        pos = [x,y]
        "鼠标左键点击"
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1)

