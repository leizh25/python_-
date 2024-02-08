# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 15:13
# Author : LeiZhuzheng
# @File : 037_爬虫_切片
# @Project : python基础

s = "helao world"
# 在切片中 直接写一个下标
print(s[0])

# 左闭右开区间
print(s[0:4])

# 从起始开始  一直到末尾
print(s[1:])

# 从下标为0的元素开始截取4个元素
print(s[:4])

#从下标为0的位置开始 到下标为6的位置结束  每次增长2个长度
print(s[0:6:2])
