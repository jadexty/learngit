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
import ctypes
from ctypes import wintypes
import logging
import sys
import os
from ctypes import *
import subprocess
import threading
import win32api

"暂停标志"
pause = False
class If_pause:
    "判断是否暂停的线程"
    def __init__(self):
        self._running = True
        print '__init__ \n'
    def terminate(self):
        self._running = False
    
    def run(self):
        "子线程只能访问主线程的global变量"
        print "self._running --->{} \n".format(self._running)
        def if_pause(self):
            n = 0 
            cols = [0,0,0,0,0,0,0,0,0,0]
            pos = (813, 762)
            while n < 10:
                print "n-->{} \n".format(n)
                col = autopy.bitmap.capture_screen().get_color(pos[0], pos[1]) 
                cols[n] = col
                print "colr -->{} \n".format(col)
                n = n + 1
                time.sleep(1)
            print "cols-->{} \n".format(cols)
            return cols          
        cols = if_pause(self)
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
        "如果一样,就给全局变量pause设置为True"
        if diff == False:
            global pause 
            pause = True
        print 'pause -->{} \n'.format(pause) 
        os.system('pause')

c = If_pause()
#t = Thread(target=c.run, args=(10,))
t = Thread(target=c.run)
t.start()
print 't.start() \n'
#c.terminate() # Signal termination
#print 'c.terminate()'
t.join()      # Wait for actual termination (if needed)
print 't.join() \n'


#由下面的输出结果可以看出,start之后,主线程和子线程交替执行.

'''
没有c.terminate()加入的执行顺序:
C:\windows\system32\cmd.exe /c (python thread_signal.py)
__init__

t.start()
self._running --->True


('T-minus', 10)
('T-minus', 9)
('T-minus', 8)
('T-minus', 7)
('T-minus', 6)
('T-minus', 5)
('T-minus', 4)
('T-minus', 3)
('T-minus', 2)
('T-minus', 1)
t.join()

Hit any key to close this window...

'''
'''
terminate加入的结果:
C:\windows\system32\cmd.exe /c (python thread_signal.py)
__init__

self._running --->True
t.start()


c.terminate()
t.join()

Hit any key to close this window...

=========================
C:\windows\system32\cmd.exe /c (python thread_signal.py)
__init__

t.start()
self._running --->True


c.terminate()
t.join()

Hit any key to close this window...

'''
