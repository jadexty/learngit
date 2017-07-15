#coding=utf-8 #后台线程
#
#默认情况下，主线程退出之后，即使子线程没有join。那么主线程结束后，子线程也依然会继续执行。如果希望主线程退出后，其子线程也退出而不再执行，则需要设置子线程为后台线程。python提供了seDeamon方法：
#
#
import threading
import random 
import time 
'''
1.开启子线程守护模式Daemon后,主线程开启5个子线程后,运行6秒结束. 5个子线程有的没有结束的,也会随着主线程结束而结束.
2.如果没有设置子线程守护模式, 则线程没有主次之分, 整个程序要等所有线程结束后,才会结束.
'''
class MyThread(threading.Thread):

    print 'MyThread'
    def run(self):
        print 'MyThread --> run'
        wait_time = random.randrange(1, 10)
        print 'thread {} will wait {}s \n'.format(self.name, wait_time)
        time.sleep(wait_time)
        print 'thread {} finished \n'.format(self.name)

def begin():
    print "begin thread"
    for i in range(5):
        t = MyThread()
        "设置为守护线程"
        t.setDaemon(True)
        t.start()
    print "wait 5 second"
    time.sleep(5)
    print "End threading"
begin()

#error:

#xception in thread Thread-5:
#Traceback (most recent call last):
#  File "C:\Python27\lib\threading.py", line 801, in __bootstrap_inner
#    self.run()
#  File "byl\thread_daemon.py", line 13, in run
#    wait_time = random.randrange(1, 10)
#NameError: global name 'random' is not defined
#解决方案:
#    import random
