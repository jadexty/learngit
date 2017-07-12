vim就是键盘上的舞蹈.

#    vim如何获取当前文件的路径?  

'''
在命令行模式下：
% 当前完整的文件名
****%:h 文件名的头部，即文件目录.例如../path/test.c就会为../path
   %:t 文件名的尾部.例如../path/test.c就会为test.c  
%:r  无扩展名的文件名.例如../path/test就会成为test
%:e 扩展名
'''

# 将所有行里面的source替换为target, 根据提示选择是否替换.
:%s/source/target/c

#ma给代码行标记a, `a就会跳回做标记的地方.
