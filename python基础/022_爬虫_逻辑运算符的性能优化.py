# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 11:01
# Author : LeiZhuzheng
# @File : 022_爬虫_逻辑运算符的性能优化
# @Project : python基础

# and性能优化 当and前面的结果是false的情况下，后面的结果是不会执行的
a = 36
a > 10 and print("hello")
a < 10 and print("hello 2")

# or性能优化
# 只要有一方为true 那么结果就是true
