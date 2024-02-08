# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 18:39
# Author : LeiZhuzheng
# @File : 056_爬虫_请求对象的定制
# @Project : python爬虫

import urllib.request

url = "https://www.baidu.com"

# url组成
# 协议  http/https
# 主机名 www.baidu.com
# 端口号   http:80   https:443
# 路径 /  /index.html
# 参数 ?a=1&b=2
# 锚点 #

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
}
# 因为urlopen中不能存储字典 所以headers不能传递进去
# 请求对象的定制
# 注意 因为参数顺序的问题  不能直接写url 和 headers   中间还有一个data
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)
