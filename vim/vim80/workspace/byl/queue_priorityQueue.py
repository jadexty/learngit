#coding=utf-8
import Queue
#默认是FIFO,如果指定是PriorityQueue,就数值小的优先级别高
q = Queue.PriorityQueue()   
#q = Queue.Queue()
# put() 参数一为优先级,第二个参数是value
q.put((3, "alex3"))
q.put((2, "alex2"))
q.put((1, "alex1"))
print(q.get())

#-----------------
#(1, 'alex1')
