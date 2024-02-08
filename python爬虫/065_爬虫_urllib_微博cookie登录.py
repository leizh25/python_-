# _*_ coding : utf-8 _*_
# @Time : 2024/2/8 0:15
# Author : LeiZhuzheng
# @File : 065_爬虫_urllib_微博cookie登录
# @Project : python爬虫

# 适用的场景: 数据采集的时候 需要绕过登录 然后进入到某个页面
# 个人信息页面是utf-8  但是还报错编码错误  因为并没有进入到个人信息页  而是跳转到了登录页面 而且登录页面不是utf-8  所以报错

# 什么情况下访问不成功?
# 1. 请求头的信息不够
import urllib.request

url = "https://weibo.cn/5297795165/info"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
    "Cookie": "SUB=_2A25Ix91sDeRhGeNM4lUW-SvNzTmIHXVrvVCkrDV6PUJbktCOLUfFkW1NSfI_RJ-TAPuYpOoW68WKtHqF173zzwur; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFkqZkvA0J.DmfdupksG.qj5JpX5KzhUgL.Fo-E1KMN1K-pSo-2dJLoI74SIgSEdEH81C-4BbHFS7tt; SSOLoginState=1707322684; ALF=1709914684;_T_WM=0794e85a796f6b0e26f4eb16294ed078",
    "Referer": "https://weibo.cn/",
}
# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)
# 获取响应内容
content = response.read().decode("utf-8")
# 将数据保存到本地
with open("weibo.html", "w", encoding="utf-8") as fp:
    fp.write(content)
