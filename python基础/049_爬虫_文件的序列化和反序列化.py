# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 17:13
# Author : LeiZhuzheng
# @File : 049_爬虫_文件的序列化和反序列化
# @Project : python基础

# 默认情况下 我们只能将字符串写入到文件中
# fp = open("test.txt", "w")
# fp.write("hello world")
# fp.close()


# fp = open("test.txt", "w")
# # 默认情况下,对象是无法写入到文件中的  如果想写入到文件  那么需要序列化操作
# name_list = ["张三", "李四", "王五"]
# fp.write(name_list)


# 序列号的两种操作
# dumps()
# # (1) 创建一个文件
# fp = open("test.txt", "w")
# # (2) 定义一个列表
# name_list = ["张三", "李四", "王五"]
#
# # 导入json模块到该文件中
# import json
#
# # 序列号
# # 将Python对象序列化为json字符串
# names = json.dumps(name_list)
#
# # 将names写入到文件中
# fp.write(names)
#
# fp.close()


# dump()
# 在将对象转换为字符串的同时,指定一个文件的对象 然后把转换后的字符串写入到文件里
# fp = open("test.txt", "w")
# name_list = ["张三", "李四", "王五"]
# # 相当于names = json.dump(name_list) 和 fp.write()
# import json
#
# json.dump(name_list, fp)
# fp.close()


# 反序列化
# 将json字符串变成一个Python对象
# fp = open("test.txt", "r")
# content = fp.read()
# # print(content)
#
# # loads
# import json
#
# # 将json字符串变成Python对象
# result = json.loads(content)
# print(result)
# print(type(result))
# fp.close()


# load
fp = open("test.txt", "r")
import json

result = json.load(fp)
print(result)
print(type(result))
fp.close()
