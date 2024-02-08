# _*_ coding : utf-8 _*_
# @Time : 2024/2/8 21:33
# Author : LeiZhuzheng
# @File : 071_爬虫_解析_获取百度网站的百度一下
# @Project : python爬虫

# 1. 获取网页源码

# 2.解析  服务器响应的文件  etree.HTML()

# 3.打印
import urllib.request

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)
# 获取网页源码
content = response.read().decode("utf-8")
# print(content)


# 解析网页源码 获取想要的数据
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据  xpath的返回值是一个列表类型的数据
result = tree.xpath("//input[@id='su']/@value")

print(result[0])
