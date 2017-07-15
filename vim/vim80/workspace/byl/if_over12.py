#coding=utf-8
#-----------------
#判断是否过了24点
#-----------------
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
i = datetime.datetime.now()

#u表明输出是中文字符串
print (u"当前的日期和时间是 %s" % i)
print (u"ISO格式的日期和时间是 %s" % i.isoformat() )
print (u"当前的年份是 %s" %i.year)
print (u"当前的月份是 %s" %i.month)
print (u"当前的日期是  %s" %i.day)
print (u"dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print (u"当前小时是 %s" %i.hour)
print (u"当前分钟是 %s" %i.minute)
print (u"当前秒是  %s" %i.second)

begin_day= i.day
print (u'begin_day is %s'%begin_day)
current_day = i.day
print (u'current_day is %s'%current_day)
def if_over24(current_day):
    if current_day != begin_day:
        return True
        print 'over 24 !!!'
    print 'not over 24'
    return True
if_over24(current_day)

