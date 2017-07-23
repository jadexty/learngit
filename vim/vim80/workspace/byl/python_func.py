# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''

'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"

'位置参数'
def power(x,n):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s

a = power(2,2)
b = power (5,3)
print 'a: {} \n'.format(a)
print 'b: {} \n'.format(b)

'默认参数'
def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s
print 'power(x,2): {} \n'.format(power(3))

'默认参数是一个list,可变参数'
def add_end(l=[]):
    l.append('end')
    return l
print 'add_end(): {} \n'.format(add_end())
print 'add_end(): {} \n'.format(add_end())
#add_end(): ['end']
#
#add_end(): ['end', 'end']

'默认参数是不可变参数'
def add_end(l=None):
    if l == None:
        l = []
    l.append('end')
    return l
print 'add_end(): {} \n'.format(add_end())
print 'add_end(): {} \n'.format(add_end())
#add_end(): ['end']
#
#add_end(): ['end']

'list或者tuple作为参数'
def calc(number):
    sum = 0
    for i in number:
        sum = sum+i
    return sum

calc([1,2,3])
print 'calc(10):{} \n'.format(calc([1,2,3]))
#calc(10):6

'可变参数*number'
def calc(*number):
    sum = 0
    for i in number:
        sum = sum+i
    return sum
calc(1,2)
print 'calc():{} \n'.format(calc())
print 'calc(1,2):{} \n'.format(calc(1,2))
print 'calc(1,2,3):{} \n'.format(calc(1,2,3))
#calc(1,2,3):6

nums = [1,2,3]
print 'calc(*nums):{} \n'.format(calc(*nums))#在list或者tuple前面加上*,就可以转入可变参数.
#calc(*nums):6

'关键字参数'
def person(name,age, **kw):
    print ('name:',name, 'age:',age, 'other:',kw)

person('Tom',20)#可以只选入必选参数
#('name:', 'Tom', 'age:', 20, 'other:', {})

person("Jason",25,city='beiJing')
#('name:', 'Jason', 'age:', 25, 'other:', {'city': 'beiJing'})
person("Adam",35,city='beiJing',gener='M',job='engeering')#任意个数的关键字参数
#('name:', 'Adam', 'age:', 35, 'other:', {'city': 'beiJing', 'gener': 'M', 'job': 'engeering'})

extra = {'city':'BeiJing','job':'Engineer'} 
person('mike',23,**extra)#组装一个dict,再传入.
#('name:', 'mike', 'age:', 23, 'other:', {'city': 'BeiJing', 'job': 'Engineer'})

'参数组合'
"按照必选,默认,可变,关键字的顺序定义参数"

def func(a,b,c=0, *arg,**kw):
    print 'a =',a,'b=',b,'c=',c,'args=',arg, 'kw=',kw

func(1,2,5,'a','b')
#a = 1 b= 2 c= 5 args= ('a', 'b') kw= {}

func(1,3,5,'a','b',x =10)
#a = 1 b= 3 c= 5 args= ('a', 'b') kw= {'x': 10}

def fun(a):
    print a
"可以随便传,但是函数内部要对参数做类型判断,才可以进行操作."
l = [1,2]
fun(l)
t = (2,3)
fun(t)
d = {'a':1,'b':2}
fun(d)
#a: 4
#
#b: 125
#
#power(x,2): 9
#
#
#
#
#calc():0
#
#calc(1,2):3
#
#
#
#Hit any key to close this window...
