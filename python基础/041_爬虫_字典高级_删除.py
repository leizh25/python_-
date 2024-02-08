# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 15:32
# Author : LeiZhuzheng
# @File : 040_爬虫_字典高级_添加
# @Project : python基础

person = {"name": "老马", "age": 18}
print(person)

# del
#   (1) 删除字典中指定的某一个元素
# del person["age"]
#   (2) 删除整个字典
# del person

# clear
#   (1) 删除字典中所有的元素, 但是保留字典对象
person.clear()

print(person)
