# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
功能:关闭通知窗口.
方案:
1. 计算各种通知窗口的特征码(哈希值)
2. 截取现在的屏幕,计算现在屏幕和通知窗口的汉明距离
2.用汉明距离来表示图像的相似性,从而知道现在的画面是哪个窗口,可以关闭.

小技巧: 开始的时候暂停足够的时间,让你去最小化shell和vim窗口.
知识:
1.在信息论中，两个等长字符串之间的汉明距离（英语：Hamming distance）
是两个字符串对应位置的不同字符的个数。换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数。

'''
__author__      = 'jade ty'

#from byl_run import shooting
import operator
from PIL import Image,ImageGrab
import itertools
from byl_run import click
import time
import os
"不能和byl_main循环导入"
#from byl_main import EXIT

"截图区域"
box= (596, 403,996, 659)
#box= (596, 403,610, 410)
def get_hash(img):
        #"计算图片的特征码,返回一个字符串"
        #image = img.convert("L")#将图片转黑白
        "按比例缩小,屏幕分辨率为1680*1050,不缩小,算出来的哈希值太大,干扰太多."
        image = img.resize((17, 11), Image.ANTIALIAS).convert("L")
        #image.show()
        #print 'image.getdata():{}'.format(image.getdata())
        pixels = list(image.getdata())#将图片数据转为list
        #print 'pixels: {}'.format(pixels)
        avg = sum(pixels) / len(pixels)#计算pixels里面元素的平均数
        #print 'avg: {}'.format(avg)
        "根据平均数avg,将pixels转为二进制字符串"
        hash =  "".join(map(lambda p : "1" if p > avg else "0", pixels))

        return hash 
def hamming_dist(tz_hash, current_hash):
"汉明距离表示图像的相似性"
    haming = sum(itertools.imap(operator.ne, tz_hash, current_hash))
    return haming 

def tz_hash():
    "计算特征图的hash, 返回一个包含hash的list"
    tz_bmp= ['screen_jjcts.bmp'] #0 金甲锤头鲨
    tz_bmp.append('screen_blv.bmp') #1 倍率道具
    tz_bmp.append('screen_jq.bmp') #2 奖券
    tz_bmp.append('screen_dst.bmp') #3 大师唐 
    tz_bmp.append('screen_zdms.bmp') #4 组队模式
    tz_bmp.append('screen_zxsc.bmp') #5 在线时长 
    tz_bmp.append('screen_zhidaole.bmp') #6 金银岛知道了
    tz_bmp.append('screen_yxgg.bmp')#7 游戏公告
    tz_bmp.append('screen_jsbs.bmp')#8 解锁比赛模式
    #tz_bmp.append('screen_mzqd.bmp')#9每周签到
    tz_bmp.append('mzqd.bmp')#9每周签到
    tz_bmp.append('ccjj_zhidaole.bmp')#10 层层晋级知道了 
    tz_bmp.append('1500wjbds.bmp')#11 1500万晋级大赛
    tz_bmp.append('blms.bmp')#12 倍率模式
    tz_bmp.append('ycgk.bmp')#13 渔村港口
    tz_bmp.append('hyxw.bmp')#14 海妖漩涡
    #tz_bmp.append()
    #tz_bmp.append()
    #tz_bmp.append()
    #tz_bmp= ['jt.bmp']
    #print 'tz_bmp:{}'.format(tz_bmp) 
    hash= []
    for i in tz_bmp:
        print 'i: {}'.format(i)
        "box表示截图的区域"
        img = Image.open('bmp\\'+i).crop(box)
        #img.show()
        hash.append(get_hash(img))
        #print 'hash: {}'.format(hash)
    #os.system('pause')
    return hash 

def hm_dic():
    "截取目前屏幕的box区域"
    print_screen = ImageGrab.grab()
    current_pic = print_screen.crop(box) 
    #current_pic.show()
    current_hash = get_hash(current_pic)

    "比较特征图和截图的相似性."
    tz_l = []#先算出来,减少循环计算
    tz_l= tz_hash()
    like= 20 #相似的汉明距离设定值,实验数据一般为5,不同就有好几十.
    "遍历所有特征图的哈希值,计算汉明距离,如果一样,就关闭对应的窗口"
    n = 0
    while n < len(tz_l):
        #print 'while n: {}'.format(n)
        h_d = hamming_dist(tz_l[n],current_hash)
        print 'h_d: {};n:{}'.format(h_d,n)
        if h_d < like:
            print 'same'
            print 'if n: {}'.format(n)
            if n == 0:#关闭金甲锤头鲨窗口
                time.sleep(1)
                click(1205, 285)
            elif n == 1:#关闭倍率道具窗口
                time.sleep(1)
                click (814, 637)
            elif n == 2:#关闭恭喜奖券窗口
                time.sleep(1)
                click(805, 641)
            elif n == 3:#关闭大师唐窗口
                time.sleep(1)
                click (1208, 284)
            elif n == 4:#关闭组队模式窗口
                time.sleep(1)
                click(1021, 363)
            elif n == 5:#关闭在线时长提示窗口
                time.sleep(1)
                click(806, 641)
            elif n == 6:#6 金银岛知道了
                time.sleep(1)
                click(810, 704)
            elif n == 7:#7 游戏公告
                time.sleep(1)
                click(1198, 305)
            elif n == 8:#8 解锁比赛模式
                time.sleep(1)
                click(1024, 364)
            elif n == 9:#9每周签到
                time.sleep(1)
                click(1195, 328)
            elif n == 10:#10 层层晋级知道了 
                time.sleep(1)
                click(809, 704)
            elif n == 11:# 1500wjbds
                time.sleep(1)
                click(812, 703)
            elif n == 12:#倍率模式
                time.sleep(1)
                click(517, 578)
            elif n == 13:#渔村港口
                time.sleep(1)
                click(799, 510)
                time.sleep(1)
                #shooting()
            elif n == 14:#海妖漩涡
                time.sleep(1)
                click(799, 510)
                shooting()
            elif n == 15:
                time.sleep(1)
                click()
        print 'diff'
        n = n + 1
    #print 't: {}'.format(t)
    #time.sleep(1)
    #click(800,600)
    #t = t + 1

if __name__ == '__main__':
    time.sleep(8)#有时间可以最小化doc窗口
    i = 0
    while i < 120:
        hm_dic()
        time.sleep(1)
        i = i+1

#i: screen_jjcts.bmp
#Traceback (most recent call last):
#  File "has_pic.py", line 157, in <module>
#    hm_dic()
#  File "has_pic.py", line 86, in hm_dic
#    tz_l= tz_hash()
#  File "has_pic.py", line 70, in tz_hash
#    img = Image.open('\\bmp\\'+i).crop(box)
#  File "C:\Python27\lib\site-packages\PIL\Image.py", line 2477, in open
#    fp = builtins.open(filename, "rb")
#IOError: [Errno 2] No such file or directory: '\\bmp\\screen_jjcts.bmp'
