#coding=utf-8
#捕鱼来了辅助
#description：
#用autopy模拟鼠标
#
#用一个进程监控游戏是否卡住,如果卡住就从头再来一次.
#
#需要进程proce_ws和proce_bg通信: 
#proce_bg告诉proce_ws,要休息多少时间,proce_ws要告诉dg画面是否暂停.
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
from multiprocessing import Process, Queue
def write_stop(que_stop):
    print 'process write_stop runing.... \n'
    '''
    每过一秒钟取pos位置的颜色,一共10秒,判断这10个颜色是否一样,
    如果一样就表示游戏已经停止了.
    ''' 
    while True:
        cols = list(range(3)) 
        pos = (813, 762)
        "每过一秒,将pos位置的color放入cols"
        n = 0
        while n < len(cols):
            #print "n-->{} \n".format(n)
            col = autopy.bitmap.capture_screen().get_color(pos[0], pos[1]) 
            cols[n] = col
            #print "col -->{} \n".format(col)
            n = n + 1
            time.sleep(1)
        #print "cols-->{} \n".format(cols)
        "判断cols里面的元素是否都一样,不一样表示画面是运动的."
        diff = False 
        #print 'diff ---> {} \n'.format(diff)
        for a in cols:
            for b in cols:
                #print 'a --> {} \n'.format(a)
                #print 'b --> {} \n'.format(b)
                #print 'a != b --> {} \n'.format(a != b) 
                if a != b:
                    diff = True 
                    break 
            break
        #print 'process ws diff--> {} \n'.format(diff) 
        "画面暂停,就给queue的右侧写个1,否则就写0"
        if diff == False:
            que_stop.append(1) 
        que_stop.append(0)
    "从queue的左侧挤出一个"
    if que_stop.appendleft() == 2:
        print'ws will pause'
        time.sleep()
    print 'ws diff--> {} \n'.format(diff) 
    #print 'ws contine'
def if_stop(que_stop):
    '等待proce_ws的结果'
    '如果取出来是true,就执行退出,通知write_stop暂停'
    if que_stop.get() == False :#只有True,才能取到数值
        print 'bg que_stop.get(True) is False '
        print 'bg put exit \n'
        que_stop.put('exit')
        exit_shouyou()
    print 'bg que_stop.get(True) == True '
    #print 'bg , put begin \n'
    #que_stop.put('begin')

def subProcess_shouyou():
    "用子进程打开手游"
    print 'subProcess_shouyou run \n'
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
    "通知proc_ws暂停,马上关闭手游了"

    os.system("taskkill /im AppMarket.exe /f")
    os.system("taskkill /im  AndroidEmulator.exe /f")
    os.system("taskkill /im  adb.exe /f")
    #subProcess_shouyou.child.kill()
    #click(1293.182) 
    #"确认"
    #click(867, 546)
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
        "判断是否卡死" 
        print 'if_stop will run \n'
        if_stop(que_stop)
        "如果玩的时间超过set_time,就退出循环."
        end_time = time.time()
        exp_time = end_time-begin_time
        #print begin_time  
        #print end_time
        #print exp_time
        #print set_time 
def if_over24(begin_day):
    "判断是否过24点,如果过24点就关闭每周签到"
    current_day = datetime.datetime.now().day
    print ('current_day --> %s \n'%current_day)
    if current_day != begin_day:
        return True
        close_weekqd()
        print 'over 24 !!! \n'
    print 'not over 24 \n'
def begin_exit(que_stop):
    "开始到结束"
    print 'begin_exit\n'
    jingru_byl(que_stop)
    time.sleep(3)
    #if_over24()

    open_beiLvMs()
    time.sleep(5)

    open_room()
    time.sleep(15)

    shooting()

    exit_shouyou()
    #os.system('pause')
def begin_begin(que_stop):
    "开始捕鱼来了,休息一下,继续"
    print 'process begin_begin runing \n'
    while True:
        "休息relax_time,再继续开始begin_exit"
        begin_exit(que_stop)
        #relax_time = 60*15
        relax_time = 5
        time.sleep(relax_time)
    
def jingru_byl(que_stop):
    "进入捕鱼来了"
    print 'jingru_byl \n'
    subProcess_shouyou()
    time.sleep(3)

    print 'open_game will run \n'
    open_game()

    "判断是否卡死" 
    print 'if_stop will run \n'
    if_stop(que_stop)

    print 'time.sleep(3)'
    time.sleep(3)

    print 'open_byl will run \n'
    open_byl()
    time.sleep(60)

    "判断是否卡死" 
    print 'if_stop will run \n'
    if_stop(que_stop)

    print 'close_gongGao will run \n'
    close_gongGao()
    time.sleep(20)

    "判断是否卡死" 
    print 'if_stop will run \n'
    if_stop(que_stop)

    close_zhiDaole()
    "判断是否卡死" 
    print 'if_stop will run \n'
    print 'close_gongGao will run \n'
    if_stop(que_stop)
#os.system("pause")

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
    exit_shouyou()
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
if __name__=='__main__':
    #游戏是否停止的信号,默认值是stop
    stop = False
    '''
    用Queue来实现在进程之间,传递信息. 
    '''
    '后进先出的queue'
    que_stop = Queue.deque()

    print 'proc_ws will start   \n'
    proc_ws= Process(target=write_stop, args=(que_stop,))
    print 'proc_bg will start \n'
    proc_bg= Process(target=begin_begin,args=(que_stop,))

    proc_ws.start()
    proc_bg.start()

    proc_bg.join()
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

