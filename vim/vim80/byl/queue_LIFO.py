#coding=utf-8
#from multiprocessing import Queue
import Queue

q = Queue.LifoQueue(3) #生成后进先出的队列,队列长度为3
print('q is empty? %s \n'%q.empty())
print('q.qsize()-->%s'%q.qsize()) 
q.put(1)  #存放第一个值到队列
q.put(2)  #存放第二个值到队列
q.put(3)  #存放第3个值到队列

print ('q -->%s'%q.print)
print('q lenth : %s \n'%q.qsize()) 

print('get frist one:%s' % q.get())  # 获取队列的第一个值
print('q.qsize()-->%s'%q.qsize()) 
print('get second on:%s ' % q.get())  # 获取队列的第二个值
print('q.qsize()-->%s'%q.qsize()) 
print('get third :%s ' % q.get())  # 获取队列的第3个值

#队列里面没有第三个,所以就一直等待.
print('get third on:%s ' % q.get())  # 获取队列的第3个值

print('q.empty()-->%s'%q.empty())
