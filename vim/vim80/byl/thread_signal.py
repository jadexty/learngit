#coding=utf-8
from threading import Thread
import time
class If_pause:
    def __init__(self):
        self._running = True
        print '__init__ \n'
    def terminate(self):
        self._running = False

    def run(self, n):
        print "self._running --->{} \n".format(self._running)
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

c = If_pause()
t = Thread(target=c.run, args=(10,))
t.start()
print 't.start() \n'
c.terminate() # Signal termination
print 'c.terminate()'
t.join()      # Wait for actual termination (if needed)
print 't.join() \n'

#由下面的输出结果可以看出,start之后,主线程和子线程交替执行.

'''
没有c.terminate()加入的执行顺序:
C:\windows\system32\cmd.exe /c (python thread_signal.py)
__init__

t.start()
self._running --->True


('T-minus', 10)
('T-minus', 9)
('T-minus', 8)
('T-minus', 7)
('T-minus', 6)
('T-minus', 5)
('T-minus', 4)
('T-minus', 3)
('T-minus', 2)
('T-minus', 1)
t.join()

Hit any key to close this window...

'''
'''
terminate加入的结果:
C:\windows\system32\cmd.exe /c (python thread_signal.py)
__init__

self._running --->True
t.start()


c.terminate()
t.join()

Hit any key to close this window...

=========================
C:\windows\system32\cmd.exe /c (python thread_signal.py)
__init__

t.start()
self._running --->True


c.terminate()
t.join()

Hit any key to close this window...

'''
