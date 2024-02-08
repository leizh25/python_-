# _*_ coding : utf-8 _*_
# @Time : 2024/2/8 0:36
# Author : LeiZhuzheng
# @File : 066_爬虫_urllib_handler处理器的基本使用
# @Project : python爬虫

# 需求: 使用handler来访问百度  获取网页源码
import urllib.request

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
}
request = urllib.request.Request(url=url, headers=headers)
# handler  build   open

# (1)获取handler对象
handler = urllib.request.HTTPHandler()
# (2)获取opener对象
opener = urllib.request.build_opener(handler)
# (3)调用open方法
response = opener.open(request)
content = response.read().decode("utf-8")
print(content)
