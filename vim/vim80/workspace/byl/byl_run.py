#coding=utf-8
#捕鱼来了辅助
#description：
#用autopy模拟鼠标
#
#用一个进程监控游戏是否卡住,如果卡住就从头再来一次.
#
#需要进程proce_ws和proce_bg通信: 
#proce_bg告诉proce_ws,要休息多少时间,proce_ws要告h诉dg画面是否暂停.
#autopy会有越界的错误提示,用cytpes就没有.
#---------------
import datetime
import win32con
import win32api 
import ctypes
from ctypes import wintypes
import logging
import time
import sys
import os
from ctypes import *
import subprocess
import threading
from win32api import GetSystemMetrics
#from multiprocessing import Process, Queue
def fenBianlv():
    "根据屏幕分辨率计算偏移系数px和py"
    "取得屏幕分辨率"
    #print "current_width =", GetSystemMetrics (0)
    width = GetSystemMetrics(0)
    #print "current_height =",GetSystemMetrics (1)
    height = GetSystemMetrics(1)
    "计算相对默认1680,  1050的偏移量"
    w = 1680.0
    h = 1050.0
    #print ('w: %s'%w)
    #print ('h: %s'%h)
    px = w/width
    py = h/height
    pxy = list(range(2)) 
    pxy[0] = px
    pxy[1] = py
    #print ('px %s'%pxy[0])
    #print ('py %s'%pxy[1])
    return pxy 
def subProcess_shouyou():
    child = subprocess.Popen(["D:\Program Files\TxGameAssistant\AppMarket\AppMarket.exe" ])
def click(x,y):
    "鼠标移动指定位置,左键点击一下"
    fbl = []
    fbl = fenBianlv()
    x1 = int(x*fbl[0]) 
    y1 = int(y*fbl[1]) 
    #print ('x1: %s \n'%x1)
    #print ('y1: %s \n'%y1)

    windll.user32.SetCursorPos(x1, y1)
    print 'mouse move to {}, {}'.format(x1,y1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1)
    #print 'mouse leftdown'
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1)
    #print 'mouse leftup'
def open_game():
    "我的游戏658, 215"
    click(658,215)
    print 'open_game \n'
def open_byl():
    "打开捕鱼来了657, 359"
    click(657, 359)
    print 'open_byl \n'
def close_gongGao():
    "关闭游戏公告1195, 302"
    click(1195, 302)
    print 'close_gongGao \n'
def close_zhiDaole():
    "关闭知道了818, 700"
    click(818, 700)
    print 'close_zhiDaole \n'
def open_beiLvMs():
    "进入倍率模式523, 627"
    click (523, 627)
    print 'open_beiLvMs \n'
def open_room():
    "进入房间 815, 522"
    click(815, 522)
    print 'open_room \n'
def close_weekqd():
    "关闭每周签到"
    click(805, 703 )
    time.sleep(3)
    click(1194, 325)
    print 'close_weekqd \n'
def if_over24(begin_day):
    "判断是否过24点,如果过24点就关闭每周签到"
    current_day = datetime.datetime.now().day
    print ('current_day --> %s \n'%current_day)
    if current_day != begin_day:
        return True
        close_weekqd()
        print 'over 24 !!! \n'
    print 'not over 24 \n'

def shooting():
    "定点循环攻击"
    x = 1287 
    y = 637 
    x1 = int(x*fenBianlv()[0])
    y1 = int(y*fenBianlv()[1])
    #autopy.mouse.move(x, y) 
    windll.user32.SetCursorPos(x1, y1)
    while True:
        pos = [x,y]
        "鼠标左键点击"
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1)

def begin_exit():
    "开始到结束"
    print 'begin_exit\n'
    jingru_byl()
    #time.sleep(3)
    ##if_over24()

    #open_beiLvMs()
    #time.sleep(5)

    #open_room()
    #time.sleep(10)

    #shooting()

def begin_begin():
    "开始捕鱼来了,休息一下,继续"
    print 'process begin_begin runing \n'
    while True:
        "休息relax_time,再继续开始begin_exit"
        begin_exit()
        #relax_time = 60*15
        relax_time = 5
        time.sleep(relax_time)
    
def jingru_byl():
    "进入捕鱼来了"
    subProcess_shouyou()
    time.sleep(3)

    open_game()
    time.sleep(3)

    open_byl()
    print 'time.sleep(70)'
    os.system('pause')
    #time.sleep(70)

    #close_gongGao()
    #print 'time.sleep(20)'
    #time.sleep(30)

    #print 'close_zhiDaole will do'
    #close_zhiDaole()
    #time.sleep(3)
    #print 'close_zhiDaole will do again..'
    #close_zhiDaole()

def checkin():
    "切换账号"
    print 'checkin \n'
    begin_day = datetime.datetime.now().day
    print ('begin_day -->%s \n'%begin_day)
    jingru_byl()
    time.sleep(3)
    open_beiLvMs()
    time.sleep(3)
    #os.system("pause")
    open_room()
    time.sleep(5)
    #os.system('pause')
    shooting()
    "退出房间"

    exit_room()
    open_set()
    time.sleep(3)
    time.sleep(2)
def open_set():
    "打开设置"
    time.sleep(3)
    click(410, 798)
    print 'open mao \n'
    time.sleep(2)
    "设置"
    click(923, 702)
    print 'open set \n'
    time.sleep(2)
    "退出登录"
    click(1067, 602)
    print 'exit denglu \n'
    time.sleep(2)
    "残忍退出"
    print 'must_exit \n'
    click(699, 640)
    time.sleep(2)
    "与qq好友玩"
    click(979, 761 )
    print 'play with qq friend \n'
    time.sleep(4)
    "切换账号"
    click(811, 844)
    print 'change acount \n' 
    time.sleep(2)
    "最后一个账号"
    click(613, 679)
    print 'last acount \n'
    if_over24(current_day)
    time.sleep(10)
    "关闭'知道了'"
    close_zhiDaole()
    print 'close_zhiDaole \n'
    "切换账号成功"
    print 'chang acount ok \n'

