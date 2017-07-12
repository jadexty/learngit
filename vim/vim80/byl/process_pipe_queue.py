#coding:utf-8
import multiprocessing
import time
from multiprocessing import Process,Queue
 
def proc1(pipe,q):
    while True:
        for i in xrange(10):
            print u"proc1 发送 %s"%i
            pipe.send(i)
            #print u'proc1 接收:',q.get(True)
            time.sleep(1)
 
def proc2(pipe,q):
    x = 2
    while True:
        print u'proc2 接收:',pipe.recv()
        time.sleep(1)
        #print u'proc2 发送:',q.put(1)
 
def proc3(pipe):
    while True:
        print u'proc3 接收:',pipe.recv()
        time.sleep(1)

if __name__ == '__main__':
# Build a pipe
    pipe = multiprocessing.Pipe()
    print pipe
     
# Pass an end of the pipe to process 1
    #p1   = multiprocessing.Process(target=proc1, args=(pipe[0],))
# Pass the other end of the pipe to process 2
    #p2   = multiprocessing.Process(target=proc2, args=(pipe[1],))

    q = Queue() 
    p3 = Process(target=proc1,args=(pipe[0],q)) 

    p4 = Process(target=proc1,args=(pipe[1],q))
     
    #p1.start()
    #p2.start()
    p3.start()
    p4.start()

    #p1.join()
    #p2.join()

#out:
#
#C:\windows\system32\cmd.exe /c (python process_pipe_queue.py)
#(<read-write PipeConnection, handle 128>, <read-write PipeConnection, handle 352
#>)
#proc1 发送 0
#proc1 发送 0
#proc1 发送 1
#proc1 发送 1
#proc1 发送 2
#proc1 发送 2
#proc1 发送 3
#proc1 发送 3
#proc1 发送 4
#proc1 发送 4
#proc1 发送 5
#proc1 发送 5
#proc1 发送 6
#proc1 发送 6
#proc1 发送 7
#proc1 发送 7
#proc1 发送 8
#proc1 发送 8
#proc1 发送 9
#proc1 发送 9
#proc1 发送 0
#proc1 发送 0
#proc1 发送 1
#proc1 发送 1
#proc1 发送 2
#proc1 发送 2
#proc1 发送 3
#proc1 发送 3
#proc1 发送 4
#proc1 发送 4
#proc1 发送 5
#proc1 发送 5
#proc1 发送 6
#proc1 发送 6
#-----------------------
#C:\windows\system32\cmd.exe /c (python process_pipe_queue.py)
#(<read-write PipeConnection, handle 128>, <read-write PipeConnection, handle 352
#>)
#Traceback (most recent call last):
#  File "process_pipe_queue.py", line 37, in <module>
#    p3 = Process(target=proc1,args=(pipe[3],q))
#IndexError: tuple index out of range
#shell returned 1
#Hit any key to close this window...
#------------------------------
#C:\windows\system32\cmd.exe /c (python process_pipe_queue.py)
#(<read-write PipeConnection, handle 128>, <read-write PipeConnection, handle 352
#>)
#proc1 发送 0
#proc2 接收: 0
#proc1 发送 0
#Process Process-3:
#Traceback (most recent call last):
#  File "C:\Python27\lib\multiprocessing\process.py", line 258, in _bootstrap
#    self.run()
#  File "C:\Python27\lib\multiprocessing\process.py", line 114, in run
#    self._target(*self._args, **self._kwargs)
#  File "C:\vim\vim80\byl\process_pipe_queue.py", line 10, in proc1
#    pipe.send(i)
#AttributeError: 'Queue' object has no attribute 'send'
#proc1 发送 0
#Process Process-4:
#Traceback (most recent call last):
#  File "C:\Python27\lib\multiprocessing\process.py", line 258, in _bootstrap
#    self.run()
#  File "C:\Python27\lib\multiprocessing\process.py", line 114, in run
#    self._target(*self._args, **self._kwargs)
#  File "C:\vim\vim80\byl\process_pipe_queue.py", line 10, in proc1
#    pipe.send(i)
#AttributeError: 'Queue' object has no attribute 'send'
#proc1 发送 1
#proc2 接收: 1
#proc1 发送 2
#proc2 接收: 2
#proc1 发送 3
#proc2 接收: 3
#proc1 发送 4
#proc2 接收: 4
#proc1 发送 5
#proc2 接收: 5
#proc1 发送 6
#proc2 接收: 6
#proc1 发送 7
#proc2 接收: 7
#proc1 发送 8
#proc2 接收: 8
#proc1 发送 9
#proc2 接收: 9
#proc1 发送 0
#proc2 接收: 0
#proc1 发送 1
#proc2 接收: 1
#proc1 发送 2
#proc2 接收: 2
#-------------------------
#C:\windows\system32\cmd.exe /c (python process_pipe.py)
#(<read-write PipeConnection, handle 128>, <read-write PipeConnection, handle 352
#>)
#proc1 发送 0
#proc1 接收proc2 接收: 0
#proc2 发送 2
# 2
#pproc2 接收:roc1 发送 1
#p roc1 接收1
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 2
#p roc1 接收2
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 3
#p roc1 接收3
#proc2 发送 2
# 2
#pproc2 接收:roc1 发送 4
# p4roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 5
#p roc1 接收5
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 6
#p roc1 接收6
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 7
#p roc1 接收7
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 8
# p8roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 9
# p9roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 0
#p roc1 接收0
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 1
# 1p
#roc1 接收proc2 发送 2
# 2
#proc2 接收:proc1 发送 2
#p roc1 接收2
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 3
# p3roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 4
#p roc1 接收4
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 5
#p roc1 接收5
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 6
# proc1 接收6
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 7
# p7
#roc1 接收proc2 发送 2
# 2
#proc2 接收:proc1 发送 8
# p8roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 9
# p9roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 0
#p roc1 接收0
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 1
# p1roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 2
# p2roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 3
#p roc1 接收3
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 4
# p4roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 5
# p5
#roc1 接收proc2 发送 2
# 2
#proc2 接收:proc1 发送 6
# p6roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 7
# p7roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 8
#p roc1 接收8
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 9
# p9roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 0
# p0roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 1
# p1roc1 接收
#proc2 发送 2
# 2
#proc2 接收:proc1 发送 2
# p2roc1 接收
#proc2 发送 2
# 2
#------------------------------------------
#C:\windows\system32\cmd.exe /c (python process_pipe.py)
#(<read-write PipeConnection, handle 128>, <read-write PipeConnection, handle 352
#>)
#发送 0
#proc1 接收proc2 接收: 0
#proc2 发送 1
# 1
#p穜oc2 接收:⑺?1
# 1p
#roc1 接收proc2 发送 1
# 1
#p穜oc2 接收:⑺?2
#p roc1 接收2
#proc2 发送 1
# 1
#穚⑺?3roc2 接收:
#p roc1 接收3
#proc2 发送 1
# 1
#proc2 接收:发送 4
#p roc1 接收4
#proc2 发送 1
# 1
#p穜oc2 接收:⑺?5
#p roc1 接收5
#proc2 发送 1
# 1
#proc2 接收:发送 6
# p6roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 7
#p roc1 接收7
#proc2 发送 1
# 1
#proc2 接收:发送 8
# 8p
#roc1 接收proc2 发送 1
# 1
#proc2 接收:发送 9
# p9roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 0
#p roc1 接收0
#proc2 发送 1
# 1
#proc2 接收:发送 1
# p1roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 2
# p2roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 3
# p3roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 4
#p 4roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 5
#p roc1 接收5
#proc2 发送 1
# 1
#proc2 接收:发送 6
# p6roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 7
#p roc1 接收7
#proc2 发送 1
# 1
#proc2 接收:发送 8
# 8p
#proc2 发送 1
#roc1 接收 1
#proc2 接收:发送 9
#p roc1 接收9
#proc2 发送 1
# 1
#proc2 接收:发送 0
# p0roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 1
# p1roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 2
# p2roc1 接收
#proc2 发送 1
# 1
#proc2 接收:发送 3
#p roc1 接收3
#proc2 发送 1
# 1
#p穜oc2 接收:⑺?4
# p4roc1 接收
#proc2 发送 1
# 1
#--------------------------------------------
#C:\windows\system32\cmd.exe /c (python process_pipe.py)
#(<read-write PipeConnection, handle 128>, <read-write PipeConnection, handle 352
#>)
#发送 0
#proc2 接收: 0
#发送 1
#proc2 接收: 1
#发送 2
#proc2 接收: 2
#发送 3
#proc2 接收: 3
#发送 4
#proc2 接收: 4
#发送 5
#proc2 接收: 5
#发送 6
#proc2 接收: 6
#发送 7
#proc2 接收: 7
#发送 8
#proc2 接收: 8
#发送 9
#proc2 接收: 9
#发送 0
#proc2 接收: 0
#发送 1
#proc2 接收: 1
#发送 2
#proc2 接收: 2
#发送 3
#proc2 接收: 3
#发送 4
#proc2 接收: 4
#发送 5
#proc2 接收: 5
#发送 6
#proc2 接收: 6
