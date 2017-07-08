#encoding=utf8
#-------------------
#autopy的找图功能
#取色是可以的.
#10秒之内,col的数值是否会变化,来判断程序是不是被卡死.
#------------------------
import autopy
import math
import time
import random
import os

n = 0 
cols = [0,0,0]
pos = (913, 801)
while n < 3:
    print "n-->{} \n".format(n)
    col = autopy.bitmap.capture_screen().get_color(pos[0], pos[1]) 
    cols[n] = col
    print "colr -->{} \n".format(col)
    n = n + 1
    time.sleep(1)
print "cols-->{} \n".format(cols)
#os.system('pause')
time.sleep(3)
n = 0
#print "t -->{} \n".format(t)

#print "hex(col) -->{} \n".format(hex(col))
#print "rgb -->{} \n".format(rgb) 
#
#colr -->15921906
#
#hex(col) -->0xf2f2f2
#
#rgb -->(0, 0, 0)
#
#Hit any key to close this window...


#rgb = autopy.color.hex_to_rgb(autopy.screen.get_color())
#print autopy.bitmap.Bitmap.open('2.png')
#str_c = autopy.bitmap.Bitmap.open('2.png').to_string()
##print c 
#print autopy.bitmap.Bitmap.from_string(c)
#object_b = autopy.bitmap.Bitmap.from_string(c)
#autopy.bitmap.capture_screen().save('print_screen.png')
    
#barrel = autopy.bitmap.Bitmap.open('2_3.png')
#barrel = autopy.bitmap.Bitmap.open('screengrab.png')
#monkey = barrel.get_portion((100,11),(10,12))
#monkey = autopy.bitmap.Bitmap.open('jinJCTS.png')
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
