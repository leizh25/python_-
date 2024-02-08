# _*_ coding : utf-8 _*_
# @Time : 2024/2/8 0:46
# Author : LeiZhuzheng
# @File : 067_爬虫_urllib_代理
# @Project : python爬虫

import urllib.request

url = "http://www.baidu.com/s?wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
}
request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)

# handler build_opener  open
proxies = {
    "http": "125.87.88.163:19824"
}
handler = urllib.request.ProxyHandler(proxies=proxies)
opemer = urllib.request.build_opener(handler)
response = opemer.open(request)
content = response.read().decode("utf-8")
with open("daili.html", "w", encoding="utf-8") as fp:
    fp.write(content)
