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
    "判断是否暂停的进程"
    n = 0 
    cols = [0,0,0,0,0,0,0,0,0,0]
    pos = (813, 762)
    "每过一秒,将pos位置的color放入cols"
    while n < 10:
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
    q = Queue()
    proc_ifStop = Process(target=if_stop, args=(q,))
    proc_ifStop.start()
    print ('q.get(True) -->%s'%q.get(True))

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
