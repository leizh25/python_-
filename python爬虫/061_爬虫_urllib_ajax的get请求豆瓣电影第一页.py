# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 22:40
# Author : LeiZhuzheng
# @File : 061_爬虫_urllib_ajax的get请求豆瓣电影第一页
# @Project : python爬虫

# get请求
# 获取豆瓣电影第一页的数据并且保存起来

import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
}

# 1.请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 2. 获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)

# 3.数据下载到本地
# open 方法默认情况下使用的是gbk编码   如果要想保存汉字 那么需要在open方法中指定编码格式为utf-8
# fp = open("豆瓣电影top20.json", "w", encoding="utf-8")
# fp.write(content)
with open("豆瓣电影top20.json", "w", encoding="utf-8") as fp:
    fp.write(content)
