# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
处理窗口停止
'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"
from PIL import Image,ImageGrab
from datetime import date,datetime
import time
import subprocess
from handle_windows import get_hash, hamming_dict,c_hash
def shut_down(t):
    print 'shutdown will come!'
    s = "shutdown -r -t "+str(t*3600)
    child = subprocess.Popen(s,shell=True)

def win_stop():
    '''
    过一段时间,取窗口哈希值,数值不变就表示停止了.
    '''
    while True:
        print 'handle win_stop will come \n'
        '取当前屏幕截图的哈希值'
        begin_hash = c_hash('middle') 
        #time.sleep(60*5)
        '休息一分钟'
        time.sleep(60*1)
        end_hash = c_hash('middle') 
        print 'stop hd: {} \n'.format(hamming_dict(begin_hash,end_hash))
        if hamming_dict(begin_hash,end_hash) < 10: 
            screen = ImageGrab.grab()
            d =str(datetime.now().month)
            d = d+'_'+str(datetime.now().day)
            d = d+'_'+str(datetime.now().hour)
            d = d+'_'+str(datetime.now().minute)
            d = d+'_'+str(datetime.now().second)
            print d
            screen.save('bmp\\screen\\'+d +'.bmp')
            '画面停止,就重启机器'
            child = subprocess.Popen('shutdown -r -t 3',shell=True)

