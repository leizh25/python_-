# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 15:32
# Author : LeiZhuzheng
# @File : 040_爬虫_字典高级_添加
# @Project : python基础


# 遍历  就出将数据一个一个的输出
person = {"name": "老马", "age": 18, "sex": "男"}
# print(person)

# (1) 遍历字典的key
# 字典.keys()方法,获取字典中所有的key值  key是一个变量的名字 key随便命名
# for key in person.keys():
#     print(key)

# (2) 遍历字典的value
# 字典.values()方法,获取字典中所有的value值  value是一个变量的名字 value随便命名
# for value in person.values():
#     print(value)

# (3) 遍历字典的key和value
# for key,value in person.items():
#     print(key,value)

# (4) 遍历字典的项/元素
for item in person.items():
    print(item)