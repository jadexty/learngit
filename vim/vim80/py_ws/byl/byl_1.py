# coding=utf-8
#捕鱼来了辅助
#description：
#用autopy模拟鼠标移动，实现自动攻击
#------------------------------
import autopy
import time

#autopy.mouse.move(957, 695) 
#time.sleep(1/3)
#autopy.mouse.click

#让鼠标在一条竖线上一边点击，一边移动
#(920, 740),(920, 680)

i = 740 
print(i)
while i >680 :
    autopy.mouse.move(920, i) 
    print ("i:  ",i)
    time.sleep(1/2)
    autopy.mouse.click
    time.sleep(1/2)
    i = i - 1 

