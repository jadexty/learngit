#coding=utf-8
#from multiprocessing import Process,Queue
import Queue
import threading
import time
#if __name__=='__main__':
q = Queue.Queue()
# 生成者(client)
def productor(arg):
    # 序号加包子,将做好的包子放到篮子(队列)里
    #put里面有中文
    q.put(str(arg) + 'bao_zi')
# 创建30个包子
for i in range(30):
    t = threading.Thread(target=productor, args=(i,))
    t.start()
# ============================================================== #
# 消费者(server)
def consumer(arg):
    while True:
        # arg(0-3)吃包子得人, q.get()从篮子(队列)里取包子,包子有序号
        #print(arg, q.get())
        print 'arg -->{}; q.get()-->{} \n'.format(arg,q.get())
        time.sleep(2)
# 三个线程一起吃包子
for j in range(3):
    t = threading.Thread(target=consumer, args=(j,))
    t.start()


#从输出可以看出,线程的执行顺序,是由操作系统控制的.
#out
#arg -->0; q.get()-->0bao_zi
#arg -->1; q.get()-->1bao_zi
#
#arg -->2; q.get()-->2bao_zi
#
#
#arg -->0; q.get()-->3bao_zi
#
#arg -->2; q.get()-->4bao_zi
#arg -->1; q.get()-->5bao_zi
#
#
#arg -->0; q.get()-->6bao_zi
#
#arg -->1; q.get()-->7bao_zi
#arg -->2; q.get()-->8bao_zi
#
#
#arg -->0; q.get()-->9bao_zi
#
#arg -->1; q.get()-->10bao_zi
#arg -->2; q.get()-->11bao_zi
#
#
#arg -->0; q.get()-->12bao_zi
#
#arg -->2; q.get()-->13bao_zi
#arg -->1; q.get()-->14bao_zi
#
#
#arg -->0; q.get()-->15bao_zi
#
#arg -->1; q.get()-->16bao_zi
#
#arg -->2; q.get()-->17bao_zi
#
#arg -->0; q.get()-->18bao_zi
#
#arg -->1; q.get()-->19bao_zi
#
#arg -->2; q.get()-->20bao_zi
#
#arg -->0; q.get()-->21bao_zi
#
#arg -->1; q.get()-->22bao_zi
#
#arg -->2; q.get()-->23bao_zi
#
#arg -->0; q.get()-->24bao_zi
#
#arg -->1; q.get()-->25bao_zi
#
#arg -->2; q.get()-->26bao_zi
#
#arg -->0; q.get()-->27bao_zi
#
#arg -->1; q.get()-->28bao_zi
#
#arg -->2; q.get()-->29bao_zi


