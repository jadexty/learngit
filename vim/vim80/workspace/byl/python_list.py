# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
list test

'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"

tz_bmp= ['screen_jjcts.bmp'] #0 金甲锤头鲨
tz_bmp.append('screen_blv.bmp') #1 倍率道具
tz_bmp.append('screen_jq.bmp') #2 奖券
tz_bmp.append('screen_dst.bmp') #3 大师唐 
tz_bmp.append('screen_zdms.bmp') #4 组队模式
tz_bmp.append('screen_zxsc.bmp') #5 在线时长 
tz_bmp.append('screen_zhidaole.bmp') #6 金银岛知道了
tz_bmp.append('screen_yxgg.bmp')#7 游戏公告
tz_bmp.append('screen_jsbs.bmp')#8 解锁比赛模式
tz_bmp.append('screen_mzqd.bmp')#9每周签到
tz_bmp.append('ccjj_zhidaole.bmp')#10 层层晋级知道了 

print 'tz_bmp:{} \n'.format(tz_bmp)

'按照索引访问list'
"first"
print 'tz_bmp[0]: {}'.format(tz_bmp[0])
'end'
print 'tz_bmp[-1]: {}'.format(tz_bmp[-1])
'增加'
tz_bmp.append('xxxx.bmp')
print 'tz_bmp: {}\n'.format(tz_bmp) 
'插入'
tz_bmp.insert(1,'x.bmp')
print 'tz_bmp: {}\n'.format(tz_bmp) 
'删除'
tz_bmp.pop()
print 'tz_bmp: {}\n'.format(tz_bmp) 
tz_bmp.pop(0)
print 'tz_bmp: {}\n'.format(tz_bmp) 

print 'list member can diff :{}'.format([1233,'dfa'])
'list长度'
print len(tz_bmp)
'排序'
tz_bmp.sort()
print 'tz_bmp.sort():{}'.format(tz_bmp)

'切片,产生新的list,end不在范围里面'
l = list(range(100))
print l
'取前面10个'
print 'fist 10:{}\n'.format(l[:10])
'后面10个'
print 'end 10:{}\n'.format(l[-10:])
'中间10-20'
print '10:20:{}\n'.format(l[10:20])
'前10个数,每两个取一个'
print ':10:2 : {} \n'.format(l[:10:2])
'所有数,每5个数,取一个'
print '::5 : {} \n'.format(l[::5])
