#coding=utf-8
#------------------------
#主线程sys.exit, 子线程byl_run不会停止.
#把它作为deamon 线程
#------------------------
import subprocess
import autopy
import time
import os,sys
import threading
from threading import Thread
import ctypes, win32con, ctypes.wintypes, win32gui
def pos_col(pos,cols):
    "每过一秒,将pos位置的color放入cols"
    n = 0
    while n < len(cols):
        #print "n-->{} \n".format(n)
        col = autopy.bitmap.capture_screen().get_color(pos[0], pos[1]) 
        cols[n] = col
        #print "col -->{} \n".format(col)
        n = n + 1
        time.sleep(1)
    print "pos:{}-->cols: {} \n".format(pos,cols)
    "判断cols里面的元素是否都一样,不一样表示画面是运动的."
    diff = False 
    for a in cols:
        for b in cols:
            #print 'a --> {} \n'.format(a)
            #print 'b --> {} \n'.format(b)
            #print 'a != b --> {} \n'.format(a != b) 
            if a != b:
                diff = True 
                break 
        break
    print 'diff--> {} \n'.format(diff) 
    if diff == False:
       return False
    return True

class Hotkey(threading.Thread):
    "注册win f3快捷键 全局变量EXIT"
    def run(self):
        global EXIT
        user32 = ctypes.windll.user32
        if not user32.RegisterHotKey(None, 99, win32con.MOD_WIN, win32con.VK_F3):
            raise RuntimeError
        try:
            msg = ctypes.wintypes.MSG()
            print msg
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        EXIT = True
                        return
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)

def if_diff():
    '''
    每过一秒钟取pos位置的颜色,一共60秒,判断这60个颜色数值是否一样,
    如果一样就表示游戏已经停止了.
    ''' 
    "问题:60秒取色也可能会一样,原因不明"
    while True:
        cols = list(range(60)) 
        pos_2 = (811, 571)
        pos_1 = (813, 762)
        "只要有一个是true,就表示画面没有停止"
        if pos_col(pos_1,cols) == True or pos_col(pos_2,cols) == True:
            return True
        return False
def byl_run(a):
        import byl_run
if __name__ == '__main__':
    EXIT = False
    hotkey = Hotkey()
    hotkey.start()
    "线程类是没有join方法的,线程函数有"
    #Hotkey.join()

    #t = Thread(target=countdown, args=(10,), daemon=True)
    th_byl=Thread(target=byl_run,args=(10,))  
    th_byl.setDaemon(True)   
    th_byl.start()
    #child = subprocess.Popen("python byl_run.py > byl_run_log",shell=True)
    #child = subprocess.Popen("python byl_run.py ",shell=True)

    child = subprocess.Popen("shutdown -r -t 3600",shell=True)
    print'EXIT == False'
    while True :
        if EXIT == True:
            print 'EXIT == True'
            sys.exit(0)

    #child = subprocess.Popen("shutdown -r -t 60",shell=True)
#
#    begin_time = time.time()
#    print ('begin_time:%s'%begin_time)
#    "画面停止,就kill所有子进程,重新开始子进程."
#    def kill_child():
#            os.system("taskkill /im AppMarket.exe /f")
#            os.system("taskkill /im  AndroidEmulator.exe /f")
#            os.system("taskkill /im  adb.exe /f")
#            #child.kill()
#            child = subprocess.Popen("python byl_run.py",shell=True)
#    while True:
#        print ('main if_diff: %s'%if_diff())
#        if if_diff() == False:
#           kill_child() 
#
#        "byl_run进行多少时间后,就关闭所有的子进程, 重新开始"
#        set_time = 60*60
#        #set_time = 10 
#        end_time = time.time() 
#        exp_time = end_time - begin_time  
#        print ('end_time: %s'%end_time)
#        print ('exp_time: %s'%exp_time)
#        print ('set_time: %s'%set_time)
#        while exp_time > set_time:
#            kill_child()
