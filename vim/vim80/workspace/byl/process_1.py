# multiprocessing.py
import os

print 'Process (%s) start...' % os.getpid()

pid = os.fork()
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)


#ERROR:
'''
pid = os.fork()
AttributeError: 'module' object has no attribute 'fork'
shell returned 1
Hit any key to close this window...
原因是windows下面python不提供fork.
'''
