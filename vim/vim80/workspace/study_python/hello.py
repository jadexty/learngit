#-*- coding:utf-8 -*-

'a test module'

__author__= 'Jade Tian' #记录你的名字.

import sys
def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('hello ,world')
    elif len(args) == 2:
        print('hello, %s!'%args[1])
    else:
        print('Too many arguments!')

#        if __name__ == '__main__':

#            test()
test()
#__xxx_是特殊类型的变量,可以被引用,但有特殊用途,比如__main__,__init__,__
#_xx是私有变量
