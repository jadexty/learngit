# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
iterator test
list,tuple, dict,set都可以迭代.

'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"
from collections import Iterable 

'string,list,tuple, set都可以迭代.'
l = list(range(10))
print 'isinstance (list(range(10))): {} \n'.format(isinstance(l,Iterable))
str  = '123'
print 'isinstance("1234"): {} \n'.format(isinstance(str,Iterable))
t =(1,2,3,4) 
print 'isinstance((1,2,3,4)): {} \n'.format(isinstance(t ,Iterable))

dic = {'1':'a','2':'b','3':'c','4':'d'}
'默认迭代key'
for key in dic:
    print (key) 
'迭代value'
for value in dic.values():
    print value
'同时迭代key和value'
for key,value in dic.items():
    print (key,value)
print "isinstance({1:'a',2:'b',3:'c',4:'d'}): {} \n".format(isinstance(dic,Iterable))
#
#IndexError: tuple index out of range
#表示dic不能被迭代
