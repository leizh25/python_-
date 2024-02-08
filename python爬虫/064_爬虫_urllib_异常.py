# _*_ coding : utf-8 _*_
# @Time : 2024/2/8 0:07
# Author : LeiZhuzheng
# @File : 064_爬虫_urllib_异常
# @Project : python爬虫

import urllib.request
import urllib.error

# url = "https://blog.csdn.net/weixin_73295475/article/details/133987840"
url = "http://www.douban111.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
}

try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    print(content)
except urllib.error.HTTPError:
    print("系统正在升级...")
except urllib.error.URLError:
    print("系统正在升级...")
