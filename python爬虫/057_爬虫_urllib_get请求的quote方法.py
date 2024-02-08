# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 20:30
# Author : LeiZhuzheng
# @File : 057_爬虫_urllib_get请求的quote方法
# @Project : python爬虫

import urllib.request
import urllib.parse

url = "https://www.baidu.com/s?wd="
# url = "https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6"
# 请求对象的定制为了解决反爬的第一种手段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
}
# 将周杰伦三个字变成Unicode编码
# 我们需要依赖urllib.parse

name = urllib.parse.quote("周杰伦")
url += name
print(url)


request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取相应的内容
content = response.read().decode("utf-8")
print(content)
