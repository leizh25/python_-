# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 0:05
# Author : LeiZhuzheng
# @File : 010_爬虫_数据类型_列表
# @Project : python基础

# list  列表
# tuple 元组
# dict 字典

# list  列表
# 应用场景: 当获取到了很多个数据的时候,我们可以将他们存储到列表中 然后直接使用列表访问
name_list = ["周杰伦", "徐良"]
print(name_list)

# tuple 元组
age_tuple = (18, 19, 20, 21)
print(age_tuple)

# dict 字典
# 应用场景: scrapy框架使用
# 格式: 变量的名字 = {key:value,key1:value1}
person = {
    'name': "红浪漫",
    'age': 18
}
print(person)
