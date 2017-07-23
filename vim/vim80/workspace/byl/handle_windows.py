# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
处理游戏窗口
'''
__author__      = 'jade ty'

import threading
import operator,os,time
from PIL import Image,ImageGrab
import itertools
from mouse_click import click
from mouse_click import shooting 
from threading import Thread
import subprocess
def shoot_napos():
    name_pos = {}
    name_pos['ts_jbbz.bmp'] = (718, 643)
    name_pos['gnjs_ylq.bmp'] = (810, 641)
    name_pos['jsp_20.bmp'] = (1187, 349)
    name_pos['byllwxy.bmp'] = (763, 578 )
    name_pos['2bjs.bmp'] = (1055, 517)
    name_pos['dptkksqp.bmp'] = (847, 242)
    name_pos['xzazxy.bmp'] = (100,100)
    #name_pos[''] = ()
    return name_pos
def shoot_hsna(reg):
    "计算特征图的hash, 返回一个包含hash的list"
    tz_bmp = []
    tz_bmp.append('ts_jbbz.bmp')#提示金币不足 
    tz_bmp.append('gnjs_ylq.bmp')#功能解锁 娱乐圈
    tz_bmp.append('jsp_20.bmp')# 解锁跑 20
    tz_bmp.append('byllwxy.bmp')#捕鱼来了无响应 
    tz_bmp.append('2bjs.bmp')#2倍解锁 
    tz_bmp.append('dptkksqp.bmp')#点炮台可以快速切炮 
    tz_bmp.append('xzazxy.bmp')#下载安装轩辕传奇 
    #tz_bmp.append('')# 
    '建立一个哈希和名称的字典'
    hs_n = {} 
    for i in tz_bmp:
        print 'i: {}'.format(i)
        "box()表示截图的区域"
        img = Image.open('bmp\\'+i).crop(box().get(reg))
        #img.show()
        #time.sleep(5)
        hs_n[get_hash(img)] = i
    #os.system('pause')
    return hs_n 
def watch_shoot():
    while True:
        #print 'watch_shoot while True \n'
        '取当前屏幕截图的哈希值'
        current_hash = c_hash('middle') 
        '取特征图的哈希值'
        h_n = shoot_hsna('middle')
        n_p= shoot_napos()
        for key,value in h_n.items():
            '和那个特征图一样'
            if same_wind(key,current_hash,20) :
                if value == 'dptkksqp.bmp':#点炮台快速切炮
                    click(971, 739)
                #如果是捕鱼来了,下载安装轩辕传奇等无法响应的画面,就重新启动机器
                if value == 'byllwxy.bmp'or value == 'xzazxy.bmp':
                    child = subprocess.Popen('shutdown -r -t 3',shell=True)
                print 'watch_shoot same'
                pos = n_p.get(value)
                x = pos[0]
                y = pos[1]
                click(x,y)
            print 'watch_shoot diff'
        time.sleep(1)
def th_shoot():
    '监控射击画面,对弹出窗口应对'
    t = Thread(target=watch_shoot)
    t.daemon = True
    #print 'th_shoot will come'
    t.start()
def box():
    "截图区域"
    region = {}
    region['left_up'] = (296, 170,588, 668)
    region['middle'] = (596, 403,996, 821)
    region['single_double'] = (814, 747,993, 821)
    return region 
def get_hash(img):
        #"计算图片的特征码,返回一个字符串"
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
        #print (len(hash))
        return hash 
def name_pos():
    name_pos = {}
    name_pos['jjcts.bmp'] = (1205, 285)  
    name_pos['gxhd_bldj.bmp'] = (814, 637)
    name_pos['gxhd_jq.bmp'] =  (805, 641)
    name_pos['dst.bmp'] = (1208, 284)
    name_pos['jszdms.bmp'] = (1021, 363)
    name_pos['ts_zxsc.bmp'] = (806, 641)
    name_pos['jyd_zdl.bmp'] = (810, 704)
    name_pos['yxgg.bmp'] = (1198, 305)
    name_pos['jsbsms.bmp'] = (1024, 364)
    name_pos['mzqd1.bmp'] = (813, 709)
    name_pos['mzqd2.bmp'] = (813, 709)
    name_pos['mzqd13467.bmp'] = (813, 709)
    name_pos['ccjj_zdl.bmp'] = (809, 704)
    name_pos['1500wjbds_zdl.bmp'] = (812, 703)
    name_pos['blms.bmp'] = (517, 578)
    name_pos['blms1.bmp'] = (517, 578)
    name_pos['blms2.bmp'] = (517, 578)
    name_pos['ycgk.bmp'] = (799, 510)
    name_pos['hyxw.bmp'] = (799, 510)
    name_pos['syzs.bmp'] = (642, 212)
    name_pos['xsyd.bmp'] = (1164, 686)
    name_pos['xsyd_xq.bmp'] = (951, 634 )
    name_pos['gbxq.bmp'] = (1188, 332 )
    name_pos['xsyd_drms.bmp'] = (881, 293)
    name_pos['xsyd_fj.bmp'] = (1169, 689)
    name_pos['byll.bmp'] = (657, 357)
    name_pos['ts_jbbz.bmp'] = (718, 643)
    name_pos['byll_after.bmp'] = (10,10)
    name_pos['ycgk_js.bmp'] = (1194, 336)
    name_pos['lwnx.bmp'] = (1192, 336)
    name_pos['byllytzyx.bmp'] = (812, 565)
    name_pos['jjcts1.bmp'] = (1296, 287)
    name_pos['syzs1.bmp'] = (656, 217)
    name_pos['heiping.bmp'] = (100,100)
    name_pos['ts_ks.bmp'] = (100,100)
    #name_pos[''] = ()
    return name_pos

def hash_name(reg):
    "计算特征图的hash, 返回一个包含hash的list"
    tz_bmp= ['jjcts.bmp'] #0 金甲锤头鲨
    tz_bmp.append('gxhd_bldj.bmp') #1 倍率道具
    tz_bmp.append('gxhd_jq.bmp') #2 奖券
    tz_bmp.append('dst.bmp') #3 大师唐 
    tz_bmp.append('jszdms.bmp') #4 组队模式
    tz_bmp.append('ts_zxsc.bmp') #5 在线时长 
    tz_bmp.append('jyd_zdl.bmp') #6 金银岛知道了
    tz_bmp.append('yxgg.bmp')#7 游戏公告
    tz_bmp.append('jsbsms.bmp')#8 解锁比赛模式
    tz_bmp.append('mzqd1.bmp')#9每周签到
    tz_bmp.append('mzqd13467.bmp')#9每周签到
    tz_bmp.append('ccjj_zdl.bmp')#10 层层晋级知道了 
    tz_bmp.append('1500wjbds_zdl.bmp')#11 1500万晋级大赛
    tz_bmp.append('blms.bmp')#12 倍率模式
    tz_bmp.append('ycgk.bmp')#13 渔村港口
    tz_bmp.append('hyxw.bmp')#14 海妖漩涡
    tz_bmp.append('syzs.bmp')# 手游助手
    tz_bmp.append('blms1.bmp')# 倍率模式1
    tz_bmp.append('blms2.bmp')# 倍率模式2
    tz_bmp.append('xsyd.bmp')# 新手引导
    tz_bmp.append('xsyd_xq.bmp')#新手引导之详情 
    tz_bmp.append('gbxq.bmp')#关闭新手引导详情页 
    tz_bmp.append('xsyd_drms.bmp')#新手引导单人模式 
    tz_bmp.append('xsyd_fj.bmp')#新手引导 解锁房间 
    tz_bmp.append('byll.bmp')#捕鱼来了 
    tz_bmp.append('ts_jbbz.bmp')#提示金币不足 
    tz_bmp.append('byll_after.bmp')#捕鱼来了之后的黑屏
    tz_bmp.append('ycgk_js.bmp')#渔村港口 解锁
    tz_bmp.append('lwnx.bmp')#龙王怒袭
    tz_bmp.append('byllytzyx.bmp')#捕鱼来了已经停止运行
    tz_bmp.append('jjcts1.bmp')#金甲锤头鲨1
    tz_bmp.append('syzs1.bmp')#手游助手1
    tz_bmp.append('heiping.bmp')#
    tz_bmp.append('ts_ks.bmp')#
    #tz_bmp.append('')#
    '建立一个哈希和名称的字典'
    hs_n = {} 
    for i in tz_bmp:
        #print 'i: {}'.format(i)
        "box()表示截图的区域"
        img = Image.open('bmp\\'+i).crop(box().get(reg))
        #img.show()
        #time.sleep(5)
        hs_n[get_hash(img)] = i
    #os.system('pause')
    return hs_n 

def hamming_dict(hash1, hash2):
    "计算汉明距离"
    haming = sum(itertools.imap(operator.ne, hash1, hash2))
    return haming 
def c_hash(reg):
    '当前窗口的哈希值'
    print 'c_hash reg:{} \n'.format(reg)
    screen = ImageGrab.grab()
    current_pic = screen.crop(box().get(reg)) 
    #print 'current_pic will show'
    #current_pic.show()
    #time.sleep(5)
    current_hash = get_hash(current_pic)
    return current_hash
def same_wind(hash,current_hash,l):
    '窗口一致判断'
    like = l 
    h_d = hamming_dict(hash,current_hash)
    print 'h_d:{} \n'.format(h_d)
    if h_d < like:
        return True
    return False
def command():
    "对窗口进行操作"
    while True:
        #current_hash = c_hash('left_up') 
        current_hash = c_hash('middle') 
        #h_n = hash_name('left_up')
        h_n = hash_name('middle')
        n_p= name_pos()
        for key,value in h_n.items():
            '和那个特征图一样'
            if same_wind(key,current_hash,20):
                pos = n_p.get(value)
                x = pos[0]
                y = pos[1]
                print 'name:{},pos:{}\n'.format(value,pos)
                '如果是黑屏或者卡死,就重新启动机器.'
                if value == 'heiping.bmp' or value =='ts_ks.bmp' :
                    child = subprocess.Popen('shutdown -r -t 3',shell=True)
                '渔村港口就转到海妖涡旋'
                if value == 'ycgk.bmp' :
                    time.sleep(1)
                    click(1097, 492)
                '龙王怒袭'
                if value == 'lwnx.bmp' :
                    time.sleep(1)
                    click(1097, 492)
                '捕鱼来了之后的黑屏,不点击'
                if value == 'byll_after.bmp':
                    continue
                '捕鱼来了'
                if value == 'byll.bmp':
                    click(x,y)
                    time.sleep(20)
                '每周签到'
                if value == 'mzqd1.bmp'or value == 'mzqd2.bmp'or value =='mzqd13467.bmp' :
                    time.sleep(1)
                    click(1195, 328)
                print 'name:{},pos:{}\n'.format(value,pos)
                '如果是渔村港口或者海妖漩涡'
                if value == 'ycgk.bmp' or value == 'hyxw.bmp':
                    '选择单人模式'
                    b = box()
                    im = Image.open('bmp\\'+'single_double.bmp').crop(b.get('single_double'))
                    #print 'im will show' 
                    #im.show()
                    #time.sleep(5)
                    hs = get_hash(im) 
                    cs = c_hash('single_double')
                    if same_wind(hs,cs,30):
                        click(898, 785)
                    time.sleep(1)
                    click(x,y)
                    time.sleep(1)
                    click(799, 510)
                    '进入房间'
                    time.sleep(20)
                    '选择10号炮和10倍率'
                    click(811, 801)
                    time.sleep(1)
                    click(809, 703)
                    time.sleep(1)
                    click(964, 805 )
                    time.sleep(1)
                    click(966, 737)
                    time.sleep(1)
                    '启动监控线程'
                    th_shoot()
                    '开始射击'
                    shooting()
                click(x,y)
                time.sleep(3)

