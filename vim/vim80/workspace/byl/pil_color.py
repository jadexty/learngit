from PIL import Image,ImageGrab
#from PIL import 

pic = ImageGrab.grab()
#pic.show()
#pic.save('print_screen.png','png')
#im = Image.open('print_screen')
#108, 228
col = pic.getpixel((108, 228))
print 'col: {}, type: {} \n'.format(col,type(col))
#28, 339
col_1 = pic.getpixel((28, 339))
print 'col_1: {}, type: {} \n'.format(col_1,type(col_1))

print cmp(col,col_1)
#print-----------------
#col: (236, 136, 0), type: <type 'tuple'>
#
#col_1: (0, 0, 0), type: <type 'tuple'>
#
#1
#Hit any key to close this window...

