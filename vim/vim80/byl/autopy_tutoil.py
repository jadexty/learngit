#encoding=utf8
#-------------------
#autopy的找图功能
#运行三次能有一次有数值对上
#------------------------
import autopy
import math
import time
import random
'''
运行三次能有一次取上数值
'''
#autopy.bitmap.capture_screen().save('print_screen.png')
#print_screen = autopy.bitmap.Bitmap.open('print_screen.png')
pos = (770, 441)
print_screen = autopy.bitmap.capture_screen()
cols = [0,0,0] 
n = 0
while n < 3:
    col = print_screen.get_color(pos[0],pos[1])
    cols[n] = col
    n = n + 1
print "print_screen --> {} \n".format(print_screen) 
print 'pos --> {} \n'.format(pos) 
print 'col--> {} \n'.format(col) 
print 'cols-> {} \n'.format(cols) 

#print autopy.color.hex_to_rgb(col)
'''
Absolute:	770, 441 (less often used)
Relative:	770, 441 (default)
Client:	770, 441 (recommended)
ClassNN:	SysListView321
Text:	FolderView
Color:	000200 (Red=00 Green=02 Blue=00)
	x: 0	y: 0	w: 1680	h: 1050
Client:	x: 0	y: 0	w: 1680	h: 1050
'''

'''
C:\windows\system32\cmd.exe /c (python autopy_tutoil.py)
<Bitmap object at 0x00000000022B6260 with resolution 16801050, 32 bits per pixel
, and 4 bytes per pixel>
3427939
0x344e63
(52, 78, 99)
Hit any key to close this window...
'''



#print autopy.color.hex_to_rgb(hex(col))
#print sect
#4887882
#0x4a954a
#[]
#Hit any key to close this window...

#Color:	4A954A (Red=4A Green=95 Blue=4A)

#print autopy.bitmap.Bitmap.open('2.png')
#str_c = autopy.bitmap.Bitmap.open('2.png').to_string()
##print c 
#print autopy.bitmap.Bitmap.from_string(c)
#object_b = autopy.bitmap.Bitmap.from_string(c)
#autopy.bitmap.capture_screen().save('print_screen.png')
    
#barrel = autopy.bitmap.Bitmap.open('2_3.png')
#monkey = autopy.bitmap.Bitmap.open('jinJCTS_1.png')
#pos = barrel.find_every_bitmap(monkey)
#print pos

#[(328, 279)]
#结果是[(101, 12)],

#def where_is_the_monkey():
#	"""Look for the monkey. Tell me if you found it."""
#	monkey = autopy.bitmap.Bitmap.open('jinJCTS_1.png')
#	barrel = autopy.bitmap.Bitmap.open('2.png')
#        #monkey = barrel.get_portion(100,100)
#
#	#pos = barrel.find_bitmap(monkey)
#	pos = barrel.find_every_bitmap(monkey)
#
#	if pos:
#		print "We found him! He's here: %s" % str(pos)
#	else:
#		print "There is no monkey... what kind of barrel is this?"
#
#where_is_the_monkey()

'''
error:
'''
#Traceback (most recent call last):
#  File "autopy_tutoil.py", line 20, in <module>
#    monkey = barrel.get_portion(100,100)
#TypeError: argument 1 must be 2-item sequence, not int
#shell returned 1
#Hit any key to close this window...
'''
solution:
'''
#http://blog.sina.com.cn/s/blog_5eeb1e2f0101ax1o.html




#print autopy.color.hex_to_rgb(autopy.screen.get_color(1,1))
#print autopy.color.hex_to_rgb(autopy.screen.get_color(543, 443))
#autopy.bitmap.capture_screen().save('screengrab.png')

#argument 1 must be 2-item sequence, not int
