# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 16:55
# Author : LeiZhuzheng
# @File : 048_爬虫_文件的读写
# @Project : python基础

# 写数据
# write方法
# fp = open("test.txt", "a")
#
# fp.write("hello world, i am here\n" * 5)
#
# fp.close()

# 如果文件存在， 会先清空原来的数据  然后再写
# 如果模式为a 那么就会追加操作

# 读数据
fp = open("test.txt", "r")
# 默认情况下  read是一字节一字节读取，效率比较低
# content = fp.read()
# print(content)

# readline是一行一行读取，但是只能读取一行
# content = fp.readline()
# print(content)


# readlines可以按照行来读取  会将所有的数据读取到  并且以一个列表的形式返回
# 而列表中的元素是一行一行的数据
constent = fp.readlines()
print(constent)
