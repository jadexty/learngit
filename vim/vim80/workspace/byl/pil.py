from PIL import Image,ImageGrab
#from PIL import 
'屏幕打印'
pic = ImageGrab.grab()
'显示图片'
#pic.show()
'保存'
#pic.save('print_screen.png','png')
'打开图片'
#im = Image.open('print_screen')
#108, 228

'取某个位置的颜色'
col = pic.getpixel((108, 228))
print 'col: {}, type: {} \n'.format(col,type(col))
#28, 339
col_1 = pic.getpixel((28, 339))
arint 'col_1: {}, type: {} \n'.format(col_1,type(col_1))
'比较两个颜色'
print cmp(col,col_1)
#print-----------------
#col: (236, 136, 0), type: <type 'tuple'>
#
#col_1: (0, 0, 0), type: <type 'tuple'>
#
#1
#Hit any key to close this window...

