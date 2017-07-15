# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
tuple test
tuple一旦初始化就不能修改
'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"

'初始化'
tuple1, tuple2 = (123, 'xyz'), (456, 'abc')
t = ()
t = (1,)
t = ('a','b',['A','B'])#'tuple里面可以有list'


#t = (a,b)#只有整数和字符串可以作为tuple的元素

'可以修改list'
t[2][0] = 'x' 
t[2][1] = 'y'

'比较两个tuple'
print cmp(tuple1, tuple2);
print cmp(tuple2, tuple1);

tuple3 = tuple2 + (786,);
print cmp(tuple2, tuple3)

tuple4 = (123, 'xyz')
print cmp(tuple1, tuple4)
print 't:{} \n'.format(t)
'切片'
t = (range(100))
print ':10 :{} \n'.format(t[:10])
'字符串也可以切片'
str = 'abcdefghijkl'
print str
print ':5 : {} \n'.format(str[:5])
#print
#-1
#1
#-1
#0
