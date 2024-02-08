# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 18:13
# Author : LeiZhuzheng
# @File : 054_爬虫_urllib_一个类型和六个方法
# @Project : python爬虫

import urllib.request

url = "http://www.baidu.com"
# 模拟浏览器向服务器发起请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response 是 HTTPResponse的类型
# print(type(response))

# 按照一个字节一个字节的去读
# content = response.read()
# print(content)


# 返回多少个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)


# content = response.readlines()
# print(content)


# 返回状态码  如果是200 那么证明逻辑没有错
# print(response.getcode())

# 返回的是url地址
# print(response.geturl())

# 获取的是一些状态信息
# print(response.getheaders())


# 一个类型   HTTPResponse
# 六个方法   read  readline readlines getcode geturl getheaders
