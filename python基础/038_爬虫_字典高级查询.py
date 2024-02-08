# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 15:21
# Author : LeiZhuzheng
# @File : 038_爬虫_字典高级查询
# @Project : python基础

# 定义一个字典
person = {"name": "LeiZhuzheng", "age": 24, "sex": True}

# 访问person的name
# print(person["name"])
# print(person["age"])

# 使用[]的方式,获取字典中不存在的key的时候，会发生异常  keyerror
# print(person["height"])


# 不能使用.的方式访问字典中的key
# print(person.name)

# print(person.get("name"))
# print(person.get("age"))

# 使用.的方式访问字典中的不存在的key的时候  会返回None
print(person.get("aa"))
