#coding=utf-8
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)... \n' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s. \n' % os.getpid()
    "将一个函数run_proc装进进程,给函数传递一个参数test"
    p = Process(target=run_proc, args=('test',))
    print 'Process will start. \n'
    p.start()
    '''
    join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    '''
    p.join()
    print 'Process end. \n'

#print
'''
C:\windows\system32\cmd.exe /c (python process_multi.py)
Parent process 2872.

Process will start.

Run child process test (1352)...

Process end.

Hit any key to close this window...
'''
