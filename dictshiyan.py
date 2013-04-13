#--coding:utf-8--
#调用

false_count = {}
def count(ascii):
    #char = chr(ascii)?
    if chr(ascii) in false_count:
        false_count[chr(ascii)] += 1  
    else :
        false_count[chr(ascii)] = 1   #创建新键 

count(107)
count(107)
count(107)
count(107)
count(108)   
print sorted(false_count.iteritems(), key=lambda d:d[1], reverse = True )  #排序并输出
