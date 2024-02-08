# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 11:08
# Author : LeiZhuzheng
# @File : 023_爬虫_输出
# @Project : python基础

# 普通输出
print("故事里的小黄花，从出生那年就飘着")

# 格式化输出
# scrapy框架的时候  excel文件 mysql数据库  redis数据库
age = 18
name = "雷总"
# print("我的年龄是" + str(18)
#  %s 代表的是字符串   %d代表的是数值
print("我的名字是%s，我的年龄是%d" % (name, age))
