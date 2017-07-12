#coding=utf-8
#----------------------
#每过10秒钟,在指定的box截图, 和保留的图对比特征值, 汉明距离小于20,表示截图和特征图一致.
#
#----------------------
'''
在信息论中，两个等长字符串之间的汉明距离（英语：Hamming distance）是两个字符串对应位置的不同字符的个数。换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数。
'''
import operator
from PIL import Image,ImageGrab
import itertools
"截图区域"
#box= (596, 403,996, 659)
box= (596, 403,610, 410)
def get_hash(img):
        "计算图片的特征码,返回一个字符串"
        image = img.convert("L")#将图片转黑白
        "按比例缩小"
        #image = img.resize((10, 10), Image.ANTIALIAS).convert("L")
        #image.show()
        #print 'image.getdata():{}'.format(image.getdata())
        pixels = list(image.getdata())#将图片数据转为list
        #print 'pixels: {}'.format(pixels)
        avg = sum(pixels) / len(pixels)#计算pixels里面元素的平均数
        print 'avg: {}'.format(avg)
        "根据平均数avg,将pixels转为二进制字符串"
        #print '"".join(map(lambda p : "1" if p > avg else "0", pixels)): {}'.format("".join(map(lambda p : "1" if p > avg else "0", pixels)))
        return "".join(map(lambda p : "1" if p > avg else "0", pixels))

def hamming_dist(tz_hash, current_hash):
    "汉明距离表示图像的相似性"
    return sum(itertools.imap(operator.ne, tz_hash, current_hash))
def tz_hash():
    "计算特征图的hash, 返回一个包含hash的list"
    tz_png = ['screen_jjcts.png','screen_blv.png','screen_jq.png']
    print 'tz_png:{}'.format(tz_png) 
    hash1 = []
    for i in tz_png:
        "box表示截图的区域"
        print 'i: {}'.format(i)
        img = Image.open(i).crop(box)
        img.show()
        hash1.append(get_hash(img))
        print 'hash1: {}'.format(hash1)
    return hash1

def img_diff():
    "截取目前屏幕的box区域"
    print_screen = ImageGrab.grab()
    current_pic = print_screen.crop(box) 
    current_pic.show()
    current_hash = get_hash(current_pic)
    "比较特征图和截图的相似性,小于50,表示一致."
    for i in tz_hash():
        #print 'i: {}'.format(i)
        #print 'hamming_dist(tz_hash,tz_hash):{},type:'.format(hamming_dist(tz_hash,current_hash),)
        print 'hamming_dist(i,current_hash): {} '.format(hamming_dist(i,current_hash)) 
        if hamming_dist(i,current_hash) < 50:
            print 'i: {}'.format(i)
            print 'same'
        print 'i: {}'.format(i)
        print 'diff'
img_diff()
#tz_hash()


#img = Image.open('bldj.png')
#print 'get_hash(img): {}, type(get_hash(img)) \n'.format(get_hash(img),type(get_hash(img))) 
#tz_hash = get_hash(img)
#current_hash = get_hash()
#"对当前屏幕的box区域截图"

'''
box是个有4个元素的tuple
Traceback (most recent call last):
  File "has_pic.py", line 39, in <module>
    current_pic = print_screen.crop(box)
  File "C:\Python27\lib\site-packages\PIL\Image.py", line 1048, in crop
    return self._new(self._crop(self.im, box))
  File "C:\Python27\lib\site-packages\PIL\Image.py", line 1062, in _crop
    x0, y0, x1, y1 = map(int, map(round, box))
ValueError: need more than 2 values to unpack
shell returned 1
Hit any key to close this window...
'''
#box= (102, 102,102,102)
#box_1= (100, 100,105, 105)
#box= (102, 102,122,122)
#box_1= (100, 100,125, 125)
#"126"
#box= (101, 101,124,124)
#box_1= (100, 100,125, 125)
#"113"
#box= (101, 101,125,125)
#box_1= (100, 100,125, 125)
#"113"
#box= (100, 100,125,125)
#box_1= (100, 100,125, 125)
#"0"
#box= (101, 101,125,125)
#box_1= (100, 100,125, 125)
#"113"
#"相差20多个像素,汉明距离就有113"
#box= (101, 101,105,105)
#box_1= (100, 100,105, 105)
#"7"
#"相差5个像素,汉明距离就有7"
#596, 403 


