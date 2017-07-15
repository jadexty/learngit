# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
学习导入模块
1.  被导入的greet模块,不能有if __name那句. 那句是为了命令行测试用的.
'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"

import greet
from greet import greeting,EXIT

# 没有导入sys模块,不能用
#sys.path
gr = greeting('tianye')
print 'gr: {}'.format(gr)
print greet.EXIT

RUN = 1
#不能访问私有的属性
#gr_1 = greeting._private_1('tianye_1') 
