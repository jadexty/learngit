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
        
    def kill_py(self):
        '退出程序'
        os.system("taskkill /im " + py_file )
        
    def IsExitCommand(self, event):
        '''
                     是否当前按下了程序定义的热键'
                      如果按下了ALT+F2，
                     如果按下了ALT+F1，
        '''
        if event.Alt == 32 and str(event.Key) == 'F2':
            print 'F2 true'
            self.kill_py()
        elif  event.Alt == 32 and str(event.Key) == 'F1':  
            print 'F1 true'
            self.run_py()
        
    
    def onKeyboardEvent(self, event): 
        
        print #处理按下的热键
        self.IsExitCommand(event)
        
    
            
        

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
    #hm.MouseAll = my_event.onMouseEvent
    #hm.HookMouse()
    
    #循环获取消息
    pythoncom.PumpMessages()
    my_event.kill_py()             
     
def handle_start_InspecEvent():
    print "开始监控（按下ALT+ F1）"
    InspectKeyAndMouseEvent()

def handle_stop_InspecEvent():
    print"停止监控  (按下ALT+ F2)"
    InspectKeyAndMouseEvent(False)   
        
          
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
        1 : handle_start_InspecEvent,
        2 : handle_stop_InspecEvent
        }    

    print "HOTKEY_ACTIONS ->" 
    print type(HOTKEY_ACTIONS) 
    print HOTKEY_ACTIONS
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
