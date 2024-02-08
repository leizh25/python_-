# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 1:02
# Author : LeiZhuzheng
# @File : 016_爬虫_类型转换_转换为布尔类型
# @Project : python基础

# 如果对非零的整数进行布尔类型转换 那么就全都是True
# a = 1
# print(type(a))
# # 将整数变为布尔类型的数据
# b = bool(a)
# print(b)
# print(type(b))


# a = 2
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))


# a = -1
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = 0
# print(type(a))
# # 在整数的范围内 0强制类型转换bool类型的结果是False
# b = bool(a)
# print(b)
# print(type(b))


# 浮点数
# 将浮点数转换为bool类型的时候 正浮点数和负浮点数的结果是True  如果是0.0  那么是False
# a = 1.0
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = -1.0
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 字符串
# 只要字符串中有内容(包括空格和0) 那么在强制类型转换bool的时候 那么就返回True
# a = "0"
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 列表
# 只要列表中有数据 那么强制类型转换为bool的时候 就返回True
# 如果列表中什么数据都没有  那么返回False
# a = []
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 元组
# 跟 列表 转换规则一样
# a = ("李逵", "蔡徐坤")
# a = ()
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 字典
# 跟 列表 转换规则一样
# a = {"name": "zhangsan", "age": 12}
# a = {}
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))


# 什么情况下是False
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
