# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
学习导入py文件

'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"

import sys

#from python_module import RUN
"不能和python_module库循环导入"

def _private_1(name):
    "私有的不能被外部访问"
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    "公有的可以被外部访问"
    print sys.path
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
#print python_module.RUN

EXIT = 0 
#命令行测试用
#if __name__ == '__main__':

