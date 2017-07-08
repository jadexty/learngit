#coding=utf-8
#捕鱼来了辅助
#description：
#用autopy模拟鼠标
#用一个进程监控游戏卡住,就从头再来一次.
#---------------
import datetime
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

def subProcess_shouyou():
    "用子进程打开手游"
    print 'subProcess_shouyou run'
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
    #child = subProcess_shouyou.child.kill()  
    #click(1293.182) 
    #"确认"
    #click(867, 546)
def open_game():
    "我的游戏658, 215"
    click(658,215)
    print 'open_game'
def open_byl():
    "打开捕鱼来了657, 359"
    click(657, 359)
    print 'open_byl'
def close_gongGao():
    "关闭游戏公告1195, 302"
    click(1195, 302)
    print 'close_gongGao'
def close_zhiDaole():
    "关闭知道了818, 700"
    click(818, 700)
    print 'close_zhiDaole'
def open_beiLvMs():
    "进入倍率模式523, 627"
    click (523, 627)
    print 'open_beiLvMs'
def open_room():
    "进入房间 815, 522"
    click(815, 522)
    print 'open_room'
def close_weekqd():
    "关闭每周签到"
    click(805, 703 )
    time.sleep(3)
    click(1194, 325)
    print 'close_weekqd'
def shooting():
    "定点循环攻击"
    x = 1287 
    y = 637 
    autopy.mouse.move(x, y) 
    "时长"
    begin_time = time.time()
    #set_time = 60*60*1.5
    set_time = 10 
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
def if_over24(begin_day):
    "判断是否过24点,如果过24点就关闭每周签到"
    current_day = datetime.datetime.now().day
    print ('current_day --> %s'%current_day)
    if current_day != begin_day:
        return True
        close_weekqd()
        print 'over 24 !!!'
    print 'not over 24'
def begin_end():
    "开始到结束"
    begin_day = datetime.datetime.now()
    jingru_byl()
    time.sleep(3)
    if_over24()
    time.sleep(3)
    open_beiLvMs()
    time.sleep(5)
    open_room()
    time.sleep(15)
    shooting()
    #exit_shouyou() 
    #print 'exit_shouyou'
    checkin()
def begin_begin():
    '''
    开始捕鱼来了,休息一下,继续
    '''
    "判断游戏是否停止了"
    if_pause()
    while True:
        "休息relax_time,再继续开始begin_end"
        print time.clock()
        begin_end()
        relax_time = 60*15
        #relax_time = 5
        time.sleep(relax_time)
def jingru_byl():
    "进入捕鱼来了"
    subProcess_shouyou()
    time.sleep(3)
    open_game()
    time.sleep(3)
    open_byl()
    time.sleep(60)
    time.sleep(3)
    close_gongGao()
    #os.system("pause")
    time.sleep(20)
    close_zhiDaole()
    #os.system("pause")
def exit_room():

def checkin():
    "切换账号"
    print 'checkin'
    begin_day = datetime.datetime.now().day
    print ('begin_day -->%s'%begin_day)
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
    exit_shouyou()
def open_set():
    "打开设置"
    time.sleep(3)
    click(410, 798)
    print 'open mao'
    time.sleep(2)
    "设置"
    click(923, 702)
    print 'open set'
    time.sleep(2)
    "退出登录"
    click(1067, 602)
    print 'exit denglu'
    time.sleep(2)
    "残忍退出"
    print 'must_exit'
    click(699, 640)
    time.sleep(2)
    "与qq好友玩"
    click(979, 761 )
    print 'play with qq friend'
    time.sleep(4)
    "切换账号"
    click(811, 844)
    print 'change acount' 
    time.sleep(2)
    "最后一个账号"
    click(613, 679)
    print 'last acount'
    if_over24(current_day)
    time.sleep(10)
    "关闭'知道了'"
    close_zhiDaole()
    print 'close_zhiDaole'
    "切换账号成功"
    print 'chang acount ok'
#begin_begin()
while True:
    checkin()
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

