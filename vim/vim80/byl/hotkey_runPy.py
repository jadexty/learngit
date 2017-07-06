#!/usr/bin/env python
# -*- coding: utf-8 -*-
#alt+f1启动记录日志到hook_log.txt, alt+f2停止记录
import pythoncom
import pyHook
import time
import os
import sys
import ctypes
from ctypes import wintypes
import win32con
import win32api 
import subprocess
py_file = 'byl_autopy.py'

def begin_byl():
    child = subprocess.Popen(["byl_autopy.bat"])
  
def kill_byl():
    "开始监控（按下ALT+ F1）"
    print "kill vimrc.exe"
    #os.system("taskkill /im vimrc.exe /f")
    #child = subprocess.Popen(["taskkill /im vimrun.exe /f"])
    sys.exit()
#def handle_stop_InspecEvent():
#    print"停止监控  (按下ALT+ F2)"
#    InspectKeyAndMouseEvent(False)   
        
          
if __name__ == "__main__":     
    '''
    Function:通过快捷键控制程序运行
    Input：NONE
    Output: NONE
    author: socrates
    '''  
    
    byref = ctypes.byref
    user32 = ctypes.windll.user32
    
    #定义快捷键
    HOTKEYS = {
               1 : (win32con.VK_F1, win32con.MOD_ALT),
               2 : (win32con.VK_F2, win32con.MOD_ALT)
               }
    print "HOTKEYS->" 
    print HOTKEYS
    #快捷键对应的驱动函数
    HOTKEY_ACTIONS = {
        1 : begin_byl, 
        2 : kill_byl
        }    

    #注册快捷键
    for id, (vk, modifiers) in HOTKEYS.items ():
        if not user32.RegisterHotKey (None, id, modifiers, vk):
            print "Unable to register id", id    
    
    #启动监听        
    try:
        msg = wintypes.MSG ()
        while user32.GetMessageA (byref (msg), None, 0, 0) != 0:
            if msg.message == win32con.WM_HOTKEY:
                action_to_take = HOTKEY_ACTIONS.get (msg.wParam)
                if action_to_take:
                    action_to_take ()

            user32.TranslateMessage (byref (msg))
            user32.DispatchMessageA (byref (msg))

    finally:
        for id in HOTKEYS.keys ():
            user32.UnregisterHotKey (None, id) 

#ImportError: DLL load failed: %1 不是有效的 Win32 应用程序。
#Hit any key to close this window...

#64位的python,装32位的pyhook模块,会报错.

#尽量复制粘贴代码,以免出错
