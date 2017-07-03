#!/usr/bin/env python
# -*- coding: utf-8 -*-
#alt+f1启动记录日志到hook_log.txt, alt+f2停止记录
import pythoncom
import pyHook
import time
#import pyhk
import os
import sys
import ctypes
from ctypes import wintypes
import win32con
import win32api 

py_file = 'byl_mouse.py'
class CrunPy:
    '''
    Function:键盘和鼠标监控类
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-09
    ''' 
    def __init__(self, filename):
        '初始化'
        self.filename = filename
        
    def run_py(self):
        '运行文件'
        os.system("python "+ py_file)
        
    def end_self(self):
        '退出程序'
        sys._exit()
    def IsNotWriteLog(self):
        '是否记录日志'
        return  self.bFlag   
        
    def IsExitCommand(self, event):
        '''
                     是否当前按下了程序定义的热键'
                      如果按下了ALT+F2，将记录日志的状态位置为True,不记录日志,
                     如果按下了ALT+F1，将记录日志状态位置为False,表示记录日志
        '''
        if event.Alt == 32 and str(event.Key) == 'F2':
            self.bFlag = True
        elif  event.Alt == 32 and str(event.Key) == 'F1':  
            self.bFlag = False 
        
    
    def onKeyboardEvent(self, event): 
        
        #处理按下的热键
        self.IsExitCommand(event)
        
    
    #默认记录
    bFlag = False
            
        

def InspectKeyAndMouseEvent():
    "启动监控"
    my_event = CrunPy(py_file)
    my_event.run_py()
     
    #创建hook句柄
    hm = pyHook.HookManager()
    
    #监控键盘
    hm.KeyDown = my_event.onKeyboardEvent
    hm.HookKeyboard()
    
    #监控鼠标
    hm.MouseAll = my_event.onMouseEvent
    hm.HookMouse()
    
    #循环获取消息
    pythoncom.PumpMessages()
    my_event.end_self()             
     
def handle_start_InspecEvent():
    "开始监控（按下ALT+ F1）"
    InspectKeyAndMouseEvent()

def handle_stop_InspecEvent():
    "停止监控  (按下ALT+ F2)"
    InspectKeyAndMouseEvent(False)   
        
          
if __name__ == "__main__":     
    '''
    Function:通过快捷键控制程序运行
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-03-09
    '''  
    
    byref = ctypes.byref
    user32 = ctypes.windll.user32
    
    #定义快捷键
    HOTKEYS = {
               1 : (win32con.VK_F1, win32con.MOD_ALT)
#               2 : (win32con.VK_F2, win32con.MOD_ALT)
               }

    #快捷键对应的驱动函数
    HOTKEY_ACTIONS = {
        1 : handle_start_InspecEvent,
#        2 : handle_stop_InspecEvent
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

