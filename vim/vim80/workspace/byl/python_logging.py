# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''

'''
__author__      = 'jade ty'
__email__ = "985991665@qq.com"


import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                #datefmt='%a, %d %b %Y %H:%M:%S',
                datefmt='%H:%M:%S',
                filename='myapp.log',
                filemode='w')

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
