#coding=utf-8
#捕鱼来了辅助
#description：
#用autopy模拟鼠标
#---------------
import win32con
import win32api 
import ctypes
from ctypes import wintypes
import logging
import autopy
import time
import sys
import os
from ctypes import *
import win32api
import subprocess
import threading
import win32api
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
    os.system("taskkill /im  adb.exe /f")
    #click(1293.182) 
    #"确认"
    #click(867, 546)
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
    set_time = 60*60*1.5
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
    #os.system("pause")
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
        print time.clock()
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
#checkin()
#open_set()
#checkin()
'''
倍率道具
识别图片,子线程.
'''
'''
登录不同的账号,各自玩指定时间.
'''
'''
热键启动或者关闭
用hotkey_runpy.py启动, alt+f1启动本程序,alt+f2结束vimrun.exe进程.
'''

'''
demeonThread exec AppMarket.exe
qiehuan ok
Hit any key to close this window...
'''

