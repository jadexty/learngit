#coding=utf-8
import subprocess
import autopy
import time
import os
def if_diff():
    '''
    每过一秒钟取pos位置的颜色,一共60秒,判断这60个颜色数值是否一样,
    如果一样就表示游戏已经停止了.
    ''' 
    "问题:60秒取色也可能会一样,原因不明"
    while True:
        cols = list(range(60)) 
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
        print "cols-->{} \n".format(cols)
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
        #print 'diff--> {} \n'.format(diff) 
        if diff == False:
           return False
        return True
         
child = subprocess.Popen("python byl_run.py",shell=True)

begin_time = time.time()
print ('begin_time:%s'%begin_time)
"画面停止,就kill所有子进程,重新开始子进程."
def kill_child():
        os.system("taskkill /im AppMarket.exe /f")
        os.system("taskkill /im  AndroidEmulator.exe /f")
        os.system("taskkill /im  adb.exe /f")
        child.kill()
        child = subprocess.Popen("python byl_run.py",shell=True)
while True:
    print ('main if_diff: %s'%if_diff())
    if if_diff() == False:
       kill_child() 

    "byl_run进行多少时间后,就关闭所有的子进程, 重新开始"
    set_time = 60*60
    #set_time = 10 
    end_time = time.time() 
    exp_time = end_time - begin_time  
    print ('end_time: %s'%end_time)
    print ('exp_time: %s'%exp_time)
    print ('set_time: %s'%set_time)
    while exp_time > set_time:
        kill_child()
