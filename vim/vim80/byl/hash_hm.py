# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
功能: 判断图像的相似性
方案: 计算图像的哈希值,然后计算汉明距离,表达相似性
在信息论中，两个等长字符串之间的汉明距离（英语：Hamming distance）是两个字符串对应位置的不同字符的个数。换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数。
'''
__author__      = 'jade ty'
import operator
from PIL import Image,ImageGrab
import itertools
from byl_run import click
import time
"不能和byl_main循环导入"
#from byl_main import EXIT

"截图区域"
box= (596, 403,996, 659)
#box= (596, 403,610, 410)
def get_hash(img):
        "计算图片的特征码,返回一个字符串"
        image = img.convert("L")#将图片转黑白
        "按比例缩小"
        #image = img.resize((10, 10), Image.ANTIALIAS).convert("L")
        #image.show()
        #print 'image.getdata():{}'.format(image.getdata())
        pixels = list(image.getdata())#将图片数据转为list
        #print 'pixels: {}'.format(pixels)
        avg = sum(pixels) / len(pixels)#计算pixels里面元素的平均数
        print 'avg: {}'.format(avg)
        "根据平均数avg,将pixels转为二进制字符串"
        #print '"".join(map(lambda p : "1" if p > avg else "0", pixels)): {}'.format("".join(map(lambda p : "1" if p > avg else "0", pixels)))
        return "".join(map(lambda p : "1" if p > avg else "0", pixels))

def hamming_dist(tz_hash, current_hash):
    "汉明距离表示图像的相似性"
    return sum(itertools.imap(operator.ne, tz_hash, current_hash))
def tz_hash():
    "计算特征图的hash, 返回一个包含hash的list"
    tz_png = ['screen_jjcts.png','screen_blv.png','screen_jq.png','screen_dst.png','screen_zdms.png']
    #print 'tz_png:{}'.format(tz_png) 
    hash1 = []
    for i in tz_png:
        "box表示截图的区域"
        print 'i: {}'.format(i)
        img = Image.open(i).crop(box)
        #img.show()
        hash1.append(get_hash(img))
        #print 'hash1: {}'.format(hash1)
    return hash1

def img_diff():
    "截取目前屏幕的box区域"
    print_screen = ImageGrab.grab()
    current_pic = print_screen.crop(box) 
    #current_pic.show()
    current_hash = get_hash(current_pic)

    "比较特征图和截图的相似性,小于1000,表示一致."
    tz_l = []#先算出来,减少循环计算
    tz_l= tz_hash()
    like_up = 1000 #相似的汉明距离设定值
    "遍历所有特征图的哈希值,计算汉明距离,如果一样,就关闭对应的窗口"
    n = 0
    while n < len(tz_l):
        print 'while n: {}'.format(n)
        h_d = hamming_dist(tz_l[n],current_hash)
        print 'h_d: {}'.format(h_d)
        if h_d < like_up:
            print 'same'
            print 'if n: {}'.format(n)
            if n == 0:
                "这个模块单独测试,有时可以,有时无法移动到指定坐标, 加入到项目中就可以."
                time.sleep(1)
                click(1205, 285)#关闭金甲锤头鲨窗口
            elif n == 1:
                "ok"
                click (814, 637)#关闭倍率道具窗口
            elif n == 2:
                click(805, 641)#关闭恭喜奖券窗口
            elif n == 3:
                click (1208, 284)#关闭大师唐窗口
            elif n == 4:
                click(1021, 363)#关闭组队模式窗口
        print 'diff'
        n = n + 1
    #print 't: {}'.format(t)
    #time.sleep(1)
    #click(800,600)
    #t = t + 1

#time.sleep(5)#有时间可以最小化doc窗口
#img_diff()
#tz_hash()

#屏幕截图几次转换,相差671,就算一样了
#
#avg: 88
#i: screen_jjcts.png
#avg: 88
#i: screen_blv.png
#avg: 196
#i: screen_jq.png
#avg: 196
#while n: 0
#h_d: 671
#same
#if n: 0
#
