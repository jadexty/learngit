#!/usr/bin/env python
# -*- coding: utf-8 -*-
#目前alt+f1可以前台打开手游运行. alt+F2没反应,阻塞在手游运行. 
#监听是利用了windows的消息机制,
#subprocess是子线程.
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
import autopy
class CInspectKeyAndMouseEvent:
    '''
    ''' 
    def __init__(self, filename):
        '初始化'
        self.filename = filename
        
    def byl(self):
        #byl {{{
        def begin_subProcess():
            "用子进程打开手游"
            print 'begin_subProcess run'
            "call 父进程会等待子进程"  
            #child = subprocess.call(["D:\Program Files\TxGameAssistant\AppMarket\AppMarket.exe"])
            "popen不会等待子进程"
            child = subprocess.Popen(["D:\Program Files\TxGameAssistant\AppMarket\AppMarket.exe" ])
        def click(x,y):
            "鼠标移动到指定位置,左键点击一下"
            autopy.mouse.move(x,y)
            autopy.mouse.click()
            autopy.mouse.toggle(True)
            time.sleep(0.2)
            autopy.mouse.toggle(False)
            time.sleep(0.2)
        def exit_shouyou():
            print 'exit_shouyou'
            "sys.exit()会关闭父进程"
            #sys.exit()退出程序"
            #sys.exit()
            os.system("taskkill /im AppMarket.exe /f")
            os.system("taskkill /im  AndroidEmulator.exe /f")
        def open_game():
            "我的游戏658, 215"
            click(658,215)
        def open_byl():
            "打开捕鱼来了657, 359"
            click(657, 359)
        def close_gongGao():
            "关闭游戏公告1195, 302"
            click(1195, 302)
        def close_zhiDaole():
            "关闭知道了818, 700"
            click(818, 700)
        def open_beiLvMs():
            "进入倍率模式523, 627"
            click (523, 627)
        def open_fangJian():
            "进入房间820, 511"
            click(820, 511)
        def close_weekqd():
            "关闭每周签到"
            click(1194, 325)
        def shooting():
            "定点循环攻击"
            x = 1287 
            y = 637 
            autopy.mouse.move(x, y) 
            "时长"
            begin_time = time.time()
            set_time = 60*60*60*1.5
            #set_time = 10 
            end_time = 0
            exp_time = end_time-begin_time
            while exp_time < set_time:
                autopy.mouse.click()
                autopy.mouse.toggle(True)
                #time.sleep(0.1)
                time.sleep(0.05)
                autopy.mouse.toggle(False)
                #time.sleep(0.01)
                time.sleep(0.05)
                "如果玩的时间超过set_time,就退出循环."
                end_time = time.time()
                exp_time = end_time-begin_time
                print begin_time  
                print end_time
                print exp_time
                print set_time 
        def begin_end():
            "开始到结束"
            "subProcess线程运行手游"
            begin_subProcess()
            "守护线程打开手游"
            #run_DaemonThread()
            "不用子线程的方式打开手游, 线程会停在run_os(),不会继续下去."
            #run_os()
            time.sleep(3)
            open_game()
            print 'open_game'
            time.sleep(5)
            open_byl()
            print 'open_byl'
            time.sleep(70)
            close_gongGao()
            print 'close_gongGao'
            #os.system("pause")
            time.sleep(25)
            close_zhiDaole()
            print 'close_zhiDaole'
            "判断过十二点,关闭每周签到"
            if False:
                time.sleep(10)
                close_weekqd()
            time.sleep(10)
            open_beiLvMs()
            print 'open_beiLvMs'
            time.sleep(5)
            open_fangJian()
            print 'open_fangJian'
            time.sleep(10)
            shooting()
            print 'shooting'
            exit_shouyou() 
            print 'exit_shouyou'
        def begin_begin():
            "开始捕鱼来了,休息一下,继续"
            while True:
                begin_end()
                #relax_time = 60*60*1.5
                relax_time = 60*15
                #relax_time = 5
                time.sleep(relax_time)
        def checkin():
            print 'checkin'
            "subProcess open shouyou"
            begin_subProcess()
            time.sleep(3)
            open_game()
            print 'open_game'
            time.sleep(10)
            open_byl()
            print 'open_byl'
            time.sleep(80)
            close_gongGao()
            print 'close_gongGao'
            #os.system("pause")
            time.sleep(25)
            close_zhiDaole()
            "退出当前帐号"
        def open_set():
            click(410, 798)
            time.sleep(2)
            "设置"
            click(923, 702)
            time.sleep(2)
            "退出登录"
            click(464, 1042)
            time.sleep(2)
            "残忍退出"
            click(699, 640)
            time.sleep(2)
            "与qq好友玩"
            click(979, 761 )
            time.sleep(3)
            "切换账号"
            click(811, 844)
            time.sleep(2)
            "第一个账号"
            click(615, 145)
            time.sleep(2)
            "关闭'知道了'"
            close_zhiDaole()
            "切换账号成功"
            print 'qiehuan ok'
        begin_begin()     
        #}}}
    def open_file(self):
        '打开文件'
        self.fobj = open(self.filename,  'w') 
    def close_file(self):
        '关闭文件'
        self.fobj.close()    
        
    def IsNotWriteLog(self):
        '是否记录日志'
        return  self.bFlag   
        
    def IsExitCommand(self, event):
        '''
                     是否当前按下了程序定义的热键'
                      如果按下了ALT+F2，将记录日志的状态位置为True,不记录日志,
                     如果按下了ALT+F1，将记录日志状态位置为False,表示记录日志
        '''
        print self.bFlag
        if event.Alt == 32 and str(event.Key) == 'F2':
            self.bFlag = True
            print time.strftime('[%Y-%m-%d %H:%M:%S]: ',time.localtime(time.time()))+ ' stop write log'
        elif  event.Alt == 32 and str(event.Key) == 'F1':  
            self.bFlag = False 
            print time.strftime('[%Y-%m-%d %H:%M:%S]: ',time.localtime(time.time()))+ ' start write log'
        
    def onMouseEvent(self, event):      
        "处理鼠标事件"
        
        #判断是否要记录日志
        if self.IsNotWriteLog():
            return True
        
        self.fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')
        self.fobj.writelines("Current Time:%s\n" % time.strftime('[%Y-%m-%d %H:%M:%S]: ',time.localtime(time.time())))
        self.fobj.writelines("MessageName:%s\n" % str(event.MessageName))
        self.fobj.writelines("Message:%d\n" % event.Message)
        self.fobj.writelines("Time_sec:%d\n" % event.Time)
        self.fobj.writelines("Window:%s\n" % str(event.Window))
        self.fobj.writelines("WindowName:%s\n" % str(event.WindowName))
        self.fobj.writelines("Position:%s\n" % str(event.Position))
        self.fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')
        return True
    
    def onKeyboardEvent(self, event): 
        
        #处理按下的热键
        self.IsExitCommand(event)
        
        #判断是否要记录日志
        if self.IsNotWriteLog():
            sys.exit()
            return True       
        '''
        一旦byl运行起来,就阻塞了.
        '''
        self.byl()
        child = subprocess.Popen(["D:\Program Files\TxGameAssistant\AppMarket\AppMarket.exe" ])

        self.fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')
        self.fobj.writelines("Current Time:%s\n" % time.strftime('[%Y-%m-%d %H:%M:%S]: ',time.localtime(time.time())))
        self.fobj.writelines("MessageName:%s\n" % str(event.MessageName))
        self.fobj.writelines("Message:%d\n" % event.Message)
        self.fobj.writelines("Time:%d\n" % event.Time)
        self.fobj.writelines("Window:%s\n" % str(event.Window))
        self.fobj.writelines("WindowName:%s\n" % str(event.WindowName))
        self.fobj.writelines("Ascii_code: %d\n" % event.Ascii)
        self.fobj.writelines("Ascii_char:%s\n" % chr(event.Ascii))
        self.fobj.writelines("Key:%s\n" % str(event.Key))
        self.fobj.writelines('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')
        return True
    
    #默认记录
    bFlag = False
        

def InspectKeyAndMouseEvent():
    "启动监控"
    my_event = CInspectKeyAndMouseEvent("D:\\hook_log.txt")
    my_event.open_file()
     
    #创建hook句柄
    hm = pyHook.HookManager()
    
    #监控键盘
    hm.KeyDown = my_event.onKeyboardEvent
    hm.HookKeyboard()
    
    #监控鼠标
    hm.MouseAll = my_event.onMouseEvent
    hm.HookMouse()
    
    #循环获取消息,消息机制
    pythoncom.PumpMessages()
    my_event.close_file()             
     
def handle_start_InspecEvent():
    "开始监控（按下alt+f1）"
    print 'alt+f1'
    print time.strftime('[%Y-%m-%d %H:%M:%S]: ',time.localtime(time.time()))+ ' start write log'
    InspectKeyAndMouseEvent()

#def handle_stop_InspecEvent():
#    "停止监控  (按下Ctrl + F2)"
#    InspectKeyAndMouseEvent(False)   
        
          
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
