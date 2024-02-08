# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 15:32
# Author : LeiZhuzheng
# @File : 040_爬虫_字典高级_添加
# @Project : python基础

person = {"name": "老马", "age": 18}
print(person)

# 给字典添加一个新的key value
# 如果使用变量名字["键"] = value , 这个键如果不存在,就会变成新增元素
person["height"] = 170
# 如果这个键存在,就会被覆盖
person["name"] = "张三"
print(person)
