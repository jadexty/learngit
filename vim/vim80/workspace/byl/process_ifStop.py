#coding=utf-8
#------------------
#子线程根据条件,将主线程的pause变量改为true, 
#------------------
import autopy
import math
import time
import random
from threading import Thread
import win32con
from multiprocessing import Process, Queue
import sys
import os
import subprocess
import win32api

def if_stop(q):
    '''
    每过一秒钟取pos位置的颜色,一共10秒,判断这10个颜色是否一样,
    如果一样就表示游戏已经停止了.
    '''
    cols = [0,0,0,0,0,0,0,0,0,0]
    n = 0
    pos = (813, 762)
    "每过一秒,将pos位置的color放入cols"
    while n < len(cols):
        print "n-->{} \n".format(n)
        col = autopy.bitmap.capture_screen().get_color(pos[0], pos[1]) 
        cols[n] = col
        print "colr -->{} \n".format(col)
        n = n + 1
        time.sleep(1)
    print "cols-->{} \n".format(cols)
    os.system('pause')
    "判断cols里面的元素是否都一样"
    diff = False 
    print 'diff ---> {} \n'.format(diff)
    for a in cols:
        for b in cols:
            print 'a --> {} \n'.format(a)
            print 'b --> {} \n'.format(b)
            print 'a != b --> {} \n'.format(a != b) 
            if a != b:
                diff = True 
                break 
        break
    print 'diff --> {} \n'.format(diff) 
    "如果一样,就给q设置为True"
    if diff == False:
        return q.put(True) 
    #os.system('pause')

if __name__=='__main__':
    "通过进程共享变量q来判断游戏是否停止"
    byl_stop = false
    q = Queue()
    proc_ifStop = Process(target=if_stop, args=(q,))
    proc_ifStop.start()
    "取出q的值给标志标量byl_stop"
    byl_stop = q.get(True)
    print ('byl_stop -->%s'%byl_stop)



    "停止proc_ifStop"
    #proc_ifStop.terminate()
