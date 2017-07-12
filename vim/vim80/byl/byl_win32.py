#------------------------------
# coding=utf-8
#捕鱼来了辅助
#目的：
#用回车键代替鼠标左键
#方向键控控制方向
#
#现在有AHK这个软件，可以获取鼠标和窗口信息。
#
#手游助手里面就有键盘替代功能,这个功能不需要了
#------------------------------

from ctypes import * 
windll.user32.SetCursorPos(100, 300)
print "windll.user32.SetCursorPos --->"  
print windll.user32.SetCursorPos
#三. 使用AutoItX实现鼠标模拟： 
#将 AutoItX3.dll 文件复制到 Windows 目录然后注册一下regsvr32.exe AutoItX3.dll

from win32com.client import Dispatch  
print "win32com.client ---> " 
print win32com.client 
def enter_game():  
    AutoItX = Dispatch( "AutoItX3.Control" )  
    print "AutoItX = Dispatch( \"AutoItX3.Control\" ) ---> " 
    print AutoItX 
    # Block All Input  
    AutoItX.BlockInput( 1 )  
    AutoItX.Sleep( 20000 )  
    print "AutoItX.WinActivate( GAME_WINDOW_TITLE, '' ) -->" 
    print AutoItX.WinActivate( GAME_WINDOW_TITLE, '' )
    if AutoItX.WinActivate( GAME_WINDOW_TITLE, '' ):  
        pass 
    else:  
        if AutoItX.WinWaitActive( GAME_WINDOW_TITLE, '', 8 ):  
            pass 
        else:  
            # Unblock input  
            AutoItX.BlockInput( 0 )  
            return False 
    AutoItX.WinSetTitle( GAME_WINDOW_TITLE, '', _pre_title )  
    AutoItX.WinSetState( _pre_title, '', AutoItX.SW_MAXIMIZE )  
    AutoItX.Sleep( 5000 )  
    AutoItX.MouseMove( 462, 396, 10 )  
    AutoItX.MouseClick( "left" )  
    AutoItX.Sleep( 1000 )  
    AutoItX.Send( GAME_ACCT_NAME )  
    AutoItX.Sleep( 1000 )  
    AutoItX.MouseMove ( 462, 472, 10 )  
    AutoItX.MouseClick( "left" )  
    AutoItX.Sleep( 1000 )  
    AutoItX.Send( GAME_ACCT_PASS )  
    AutoItX.Send( "{ENTER}" )  
    AutoItX.Sleep( 10000 )  
    # Unblock input  
    AutoItX.BlockInput( 0 )  
    return True
enter_game()
#
#错误
#C:\windows\system32\cmd.exe /c (python buyulai_1.py)
#Traceback (most recent call last):
#  File "buyulai_1.py", line 15, in <module>
#    from win32com.client import Dispatch
#ImportError: No module named win32com.client
#shell returned 1
#Hit any key to close this window...
#解决：安装pywin32

