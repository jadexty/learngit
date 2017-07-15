# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
dict test 
和list比较，dict有以下几个特点：
只有整数和字符串才可以作为key

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。
需要牢记的第一条就是dict的key必须是不可变对象
'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"

'初始化'
d = {'Micheal':90,'jade':100} 
d1 = {1:10}
print 'd1: {}'.format(d1)
d2 = {1.1: 100}
print 'd2: {}'.format(d2)

'查找'
print 'd["jade"]: {} \n'.format(d['jade'])
print 'd["jade"]: {} \n'.format(d["jade"])
print 'd["jade"]: {} \n'.format(d.get("jade"))
print 'd["jade"]: {} \n'.format(d.get("Thomas"))

'增加'
d['Adam'] = 80
print 'd:{}'.format(d)
'修改'
d['Adam'] = 88
print 'd:{}'.format(d)
'删除'
d.pop('Micheal')
print 'd:{}'.format(d)
'list不能作为key'
l = [1,2]
#d[l] = 'a list'
