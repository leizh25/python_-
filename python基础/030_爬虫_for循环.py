# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 11:50
# Author : LeiZhuzheng
# @File : 030_爬虫_for循环
# @Project : python基础

# 循环字符串
# range(5)
# range(1, 6)
# range(1, 10, 3)
# 循环一个列表


# 一个一个的输出  叫做循环  也叫做遍历
s = "china"

# for

# 格式: for 变量 in 要遍历的数据:
#             方法体

# for i in s:
#     print(i)


# range方法的结果是一个可以遍历的对象
# for i in range(5):
#     print(i)

# range(起始值,结束值)
# 左闭右开区间
# for i in range(1, 6):
#     print(i)

# range(起始值,结束值,步长)
# for i in range(1, 10, 3):
#     print(i)

# 应用场景 会爬取一个列表返回给我们
# 循环一个列表
a_list = ["周杰伦", "林俊杰", "陶喆"]
# 遍历列表中的元素
# for i in a_list:
#     print(i)

# 遍历列表中的下标
# 判断列表中元素的个数
# print(len(a_list))

for i in range(len(a_list)):
    print(i)
