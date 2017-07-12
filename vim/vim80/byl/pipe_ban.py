import os
import time
 
fd  = os.pipe()
pid = os.fork()
 
if pid == 0:
    os.close(fd[1])
    while True:
        msg = os.read(fd[0], 1024)
        print msg
        if msg == 'q':
            os.close(fd[0])
            break
else:
    os.close(fd[0])
    while True:
        str1 = raw_input(">")
        os.write(fd[1], str1)
        if str1 == "q":
            os.close(fd[1])
            os.wait()
            break
        time.sleep(0.2)
