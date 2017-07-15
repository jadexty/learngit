#coding=utf-8
#----------
#获取屏幕分辨率
#
#
#
#----------
import os
#import wx
from win32api import GetSystemMetrics

print "width =", GetSystemMetrics (0)
print "height =",GetSystemMetrics (1)


#--------------
#width = 1680
#height = 1050
