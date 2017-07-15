#coding=utf-8
import Queue
q= Queue.deque()          #双向队列

'添加到deque的右侧'
q.append((123))
q.append(('123'))
q.append(456)
'添加到deque的左侧'
q.appendleft(789)
print(list(q))

q.pop()#从右侧挤出一个
print(list(q))

q.popleft()#从左侧挤出一个
print(list(q))

q.extend('123')#迭代式添加'123' 
print ("q.extend('123')-->%s"%q.extend('123'))
q.count(123)

"统计123有几个"
print ('q.count(123)-->%s'%q.count(123))
print(list(q))

"移除'1'"
q.remove('1')
print(list(q))

"反转这个队列"
q.reverse()
print(list(q))

#元素向右侧移动1个位置,会从左侧回来哦
q.rotate(1)
print(list(q))

#Deque 的最大长度。如果没有边界，则返回None。
print('q.maxlen %s'%q.maxlen)
#-----------------------
#[456, 123, 234]
#[456, 123]
#[123]
#q.extend('123')None
#q.count(123)1
#Hit any key to close this window...
