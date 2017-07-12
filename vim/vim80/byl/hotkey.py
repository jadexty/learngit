#coding=utf-8
#-------------
#pywin32包能够方便的引入dll并调用其中的api函数，查看MSDN，可以知道RegisterHotKey来自user32.dll文件，它的参数分别是窗口句柄、快捷键标示、组合键和虚拟键。我在消息队列中等待处理事件，如果标示符合，就执行我们自己的代码，否则继续传给系统。具体我也不多解释了，找本Windows编程的书看看就明白了（别找Visual xxx快速入门之类的，那是学龄前孩子看的），记住判断快捷键冲突，程序完事了要释放快捷键就好了。Win + F3退出程序，希望你看代码发现了这个#
#win+F3
#-------------

import ctypes, win32con, ctypes.wintypes, win32gui
import threading
import sys
EXIT = False
class Hotkey(threading.Thread):
    def run(self):
        global EXIT
        user32 = ctypes.windll.user32
        if not user32.RegisterHotKey(None, 99, win32con.MOD_WIN, win32con.VK_F3):
            raise RuntimeError
        try:
            msg = ctypes.wintypes.MSG()
            print msg
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        EXIT = True
                        return
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)
hotkey = Hotkey()
hotkey.start()
while True:
    print 'runing----------' 
    if EXIT == True:
        sys.exit(0)
