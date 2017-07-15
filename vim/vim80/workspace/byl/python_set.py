# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
set test
set 是只有key的dict, key不能重复,没有顺序

'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"

"初始化"
s = set(['1','2','3'])
print 's: {}'.format(s)
s = set([1,2,3])
print 's: {}'.format(s)

'增加'
s.add(4)
print 's: {}'.format(s)

'重复的key会被过滤'
s.add(4)
print 's: {}'.format(s)

'删除'
s.remove(1)
print 's: {}'.format(s)

