# _*_ coding : utf-8 _*_
# @Time : 2024/2/8 0:57
# Author : LeiZhuzheng
# @File : 068_爬虫_urllib_代理池
# @Project : python爬虫
import urllib.request

proxies_pool = [
    {"http": "125.87.88.163:19824"},
    {"http": "111.111.111.111:19824"},
    {"http": "222.222.222.222:19824"},
]

import random

proxies = random.choice(proxies_pool)
url = "http://www.baidu.com/s?wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
}
request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode("utf-8")

with open("dailichi.html", "w", encoding="utf-8") as fp:
    fp.write(content)
