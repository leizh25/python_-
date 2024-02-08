# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 18:02
# Author : LeiZhuzheng
# @File : 053_爬虫_urllib_基本使用
# @Project : python爬虫

# 使用urllib来获取百度首页源码
import urllib.request

# (1)定义一个url
url = 'http://www.baidu.com'

# (2)模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# (3)获取响应中的页面源码
# read 方法 返回的是字节形式的二进制数据
# 我们要将二进制数据转换为字符串
# 二进制 --> 字符串   解码  decode("")
content = response.read().decode('utf-8')

print(content)
