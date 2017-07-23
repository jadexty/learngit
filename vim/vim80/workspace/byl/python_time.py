#!/usr/bin/python
# -*- coding: UTF-8 -*-#
import datetime
import time
localtime = time.localtime(time.time())

#time.struct_time(tm_year=2017, tm_mon=7, tm_mday=19, tm_hour=21, tm_min=55, tm_s
#ec=28, tm_wday=2, tm_yday=200, tm_isdst=0)
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)
#褰撳墠鐨勬棩鏈熷拰鏃堕棿鏄?2017-07-19 21:59:45.604000
#ISO鏍煎紡鐨勬棩鏈熷拰鏃堕棿鏄?2017-07-19T21:59:45.604000
#褰撳墠鐨勫勾浠芥槸 2017
#褰撳墠鐨勬湀浠芥槸 7
#褰撳墠鐨勬棩鏈熸槸  19
#dd/mm/yyyy 鏍煎紡鏄? 19/7/2017
#褰撳墠灏忔椂鏄?21
#褰撳墠鍒嗛挓鏄?59
#褰撳墠绉掓槸  45

