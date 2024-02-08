# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 21:02
# Author : LeiZhuzheng
# @File : 059_爬虫_urllib_post请求
# @Project : python爬虫

import urllib.request
import urllib.parse

# post 请求
url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
}
data = {
    "kw": "python"
}
# post 请求的参数 必须要进行编码
# post请求的参数必须要进行编码
data = urllib.parse.urlencode(data).encode("utf-8")
# print(data)
# post请求的参数是不会拼接在url中的  而是放在请求对象定制的参数中
request = urllib.request.Request(url, data, headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 读取响应内容
content = response.read().decode("utf-8")
# 字符串变成json对象
import json

obj = json.loads(content)
print(obj)
print(type(obj))

# post请求方式的参数 必须编码  data = urllib.parse.urlencode(data)
# 编码之后必须调用的encode方法 data = urllib.parse.urlencode(data).encode("utf-8")
# 参数是放在请求对象定制的方法中 request = urllib.request.Request(url, data, headers)
