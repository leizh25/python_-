# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 15:32
# Author : LeiZhuzheng
# @File : 040_爬虫_字典高级_添加
# @Project : python基础

# 使用函数来计算1和2的和
# def sum():
#     a = 1
#     b = 2
#     c = a + b
#     print(c)


def sum(a, b):
    c = a + b
    print(c)


# 位置传参   按照位置一一对应的关系来传递参数
sum(1, 2)

# 关键字传参
sum(b=1, a=2)
