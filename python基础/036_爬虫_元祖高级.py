# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 15:05
# Author : LeiZhuzheng
# @File : 036_爬虫_元祖高级
# @Project : python基础

# a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(a_tuple[0])
# print(a_tuple[1])
# 元祖是不可以修改里面的内容的
# a_tuple[3] = 5
# print(a_tuple)

# a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a_list[0])
# a_list[3] = 5
# print(a_list)
# 列表中的元素是可以修改的  而元组中的元素不可以修改

a_tuple = (1)
print(type(a_tuple))
# 当元组中只有一个元素的时候  那么他是整形的数据
# 定义只有一个元素的元组,需要在唯一的元素后写一个逗号
b_tuple = (5,)
print(type(b_tuple))
