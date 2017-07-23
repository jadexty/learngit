# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
control alay
热键起到了关闭线程的作用,原因还不了解.
'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"

import subprocess,time,os,sys
import threading
from threading import Thread
import ctypes, win32con, ctypes.wintypes, win32gui
from PIL import Image,ImageGrab
from handle_windows import command
from mouse_click import click
#from handle_stop import shut_down
import handle_stop 
#from handle_stop import win_stop


def th_hotkey():
    "启动热键线程"
    class Hotkey(threading.Thread):
        "继承实现一个线程类, 注册f3作为热键."
        def run(self):
            global EXIT
            user32 = ctypes.windll.user32
            if not user32.RegisterHotKey(None, 99, win32con.MOD_WIN, win32con.VK_F3):
                print 'register win f3 ok'
                raise RuntimeError
            try:
                msg = ctypes.wintypes.MSG()
                print msg
                while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                    if msg.message == win32con.WM_HOTKEY:
                        print 'msg.wParam: {}'.format(msg.wParam) 
                        if msg.wParam == 99:
                            EXIT = True
                            return
                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageA(ctypes.byref(msg))
            finally:
                user32.UnregisterHotKey(None, 1)
    EXIT = False
    hotkey = Hotkey()
    hotkey.start()
def th_conWin():
    '对游戏窗口进行点击的线程'
    th_cW = Thread(target=command)
    th_cW.daemon = True
    th_cW.start()
def th_stop():
    '判断画面时候停止'
    t = Thread(target=handle_stop.win_stop)
    t.daemon = True
    t.start()
    
def subProcess_shouyou():
    "子进程启动手游助手"
    child = subprocess.Popen(["D:\Program Files\TxGameAssistant\AppMarket\AppMarket.exe" ])
if  __name__ == '__main__':
    time.sleep(9)
    #'注册热键' 
    EXIT = False#退出标志默认False
    th_hotkey()

    '打开手游助手'
    subProcess_shouyou()
    '控制窗口'
    th_conWin()
    '处理停止'
    th_stop() 
    '让handle_windows来处理'
    #handle_stop.shut_down(1)

