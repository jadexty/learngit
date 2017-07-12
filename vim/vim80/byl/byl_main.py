#coding=utf-8
#------------------------
#主线程sys.exit, 守护线程byl_run也会停止.
#------------------------
import subprocess
import autopy
import time
import os,sys
import threading
from threading import Thread
import ctypes, win32con, ctypes.wintypes, win32gui
from PIL import Image,ImageGrab
def kill_child():
            os.system("taskkill /im AppMarket.exe /f")
            os.system("taskkill /im  AndroidEmulator.exe /f")
            os.system("taskkill /im  adb.exe /f")
            child.kill()
            child = subprocess.Popen("python byl_run.py",shell=True)

def pos_col(pos,cols):
    "每过一秒,将pos位置的color放入cols"
    n = 0
    while n < len(cols):
        #print "n-->{} \n".format(n)
        #col = autopy.bitmap.capture_screen().get_color(pos[0], pos[1]) 
        "打印屏幕" 
        pic = ImageGrab.grab()
        col = pic.getpixel((pos[0],pos[1]))
        #print 'col: {} \n'.format(col)
        cols[n] = col
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
    while True:
        cols = list(range(60)) 
        pos_2 = (811, 571)
        pos_1 = (813, 762)
        "只要有一个是true,就表示画面没有停止"
        print 'pos_col(pos_1,cols): {}'.format(pos_col(pos_1,cols))
        print 'pos_col(pos_2,cols): {}'.format(pos_col(pos_2,cols))
        if pos_col(pos_1,cols) == True or pos_col(pos_2,cols) == True:
           continue 
        kill_child() 


def byl_run(a):
    "导入byl_run"
    import byl_run
    #from byl_run import shooting
if __name__ == '__main__':
    "设置热键,设置线程退出标识为False"
    EXIT = False
    hotkey = Hotkey()
    hotkey.start()
    "线程class是没有join方法的,线程function有"
    #Hotkey.join()

    "守护线程方式启动byl"
    th_byl=Thread(target=byl_run,args=(10,))  
    th_byl.setDaemon(True)   
    th_byl.start()
    #child = subprocess.Popen("python byl_run.py > byl_run_log",shell=True)
    #child = subprocess.Popen("python byl_run.py ",shell=True)
    
    "画面停止,就kill所有子进程,重新开始."
    th_ifDiff = Thread(target=if_diff)
    th_ifDiff.daemon = True
    th_ifDiff.start()

    "一个小时后重新启动电脑"
    child = subprocess.Popen("shutdown -r -t 7200",shell=True)

    "byl_run进行多少时间后,就关闭所有的子进程, 重新开始"
    print 'exp_time will start'
    begin_time = time.time()
    print ('begin_time:%s'%begin_time)
    set_time = 60*60
    #set_time = 10 
    print ('set_time: %s'%set_time)
    end_time = time.time() 
    exp_time = end_time - begin_time  
    while True:
        end_time = time.time() 
        exp_time = end_time - begin_time  
        #print ('end_time: %s'%end_time)
        print ('exp_time: %s'%exp_time)
        print ('set_time: %s'%set_time)
        print 'exp_time > set_time: {}'.format(exp_time > set_time)
        time.sleep(20)
        while exp_time > set_time:
            end_time = time.time() 
            exp_time = end_time - begin_time  
            kill_child()
        
