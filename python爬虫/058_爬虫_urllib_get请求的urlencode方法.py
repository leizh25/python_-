# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 20:47
# Author : LeiZhuzheng
# @File : 058_爬虫_urllib_get请求的urlencode方法
# @Project : python爬虫

# urlencode应用场景: 多个参数的时候

# https://www.baidu.com/s?wd=周杰伦&sex=男

# import urllib.parse
#
# data = {
#     "wd": "周杰伦",
#     "sex": "男",
#     "address": "中国台湾"
# }

# a = urllib.parse.urlencode(data)
# print(a)

# 获取 https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&address=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE的网页源码

import urllib.parse
import urllib.request

base_url = "https://www.baidu.com/s?"
data = {
    "wd": "周杰伦",
    "sex": "男",
    "address": "中国台湾"
}
new_data = urllib.parse.urlencode(data)
# print(new_data)
# 请求资源路径
url = base_url + new_data
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发请求
response = urllib.request.urlopen(request)

# 获取网页源码数据
content = response.read().decode("utf-8")
print(content)
