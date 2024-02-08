# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 0:13
# Author : LeiZhuzheng
# @File : 011_爬虫_查看变量的数据类型
# @Project : python基础

# int
# float
# boolean
# string
# list
# tuple
# dict

# type方法判断变量的数据类型
# 格式: type(变量)

# int
a = 1
print(a)
# <class 'int'>
print(type(a))

# float
b = 1.2
print(b)
# <class 'float'>
print(type(b))

# boolean
c = True
print(c)
# <class 'bool'>
print(type(c))

# string
d = "中国"
print(d)
# <class 'str'>
print(type(d))

# list
e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(e)
# <class 'list'>
print(type(e))

# tuple
f = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f)
# <class 'tuple'>
print(type(f))

# dict
g = {"name": "张三"}
print(g)
# <class 'dict'>
print(type(g))
