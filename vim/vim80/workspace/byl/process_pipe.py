#coding:utf-8
import multiprocessing
import time
 
def proc1(pipe):
    while True:
        for i in xrange(10):
            print u"proc1 发送 %s"%i
            pipe.send(i)
            time.sleep(1)
 
def proc2(pipe):
    x = 2
    while True:
        print u'proc2 接收:',pipe.recv()
        time.sleep(1)
 
def proc3(pipe):
    while True:
        print u'proc3 接收:',pipe.recv()

        time.sleep(1)

if __name__ == '__main__':
# Build a pipe
    pipe = multiprocessing.Pipe()
    print pipe
     
# Pass an end of the pipe to process 1
    p1   = multiprocessing.Process(target=proc1, args=(pipe[0],))
# Pass the other end of the pipe to process 2
    p2   = multiprocessing.Process(target=proc2, args=(pipe[1],))
     
     
    p1.start()
    p2.start()
    p1.join()
    p2.join()

#out:

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
