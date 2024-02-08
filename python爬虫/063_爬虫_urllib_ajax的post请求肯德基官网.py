# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 23:47
# Author : LeiZhuzheng
# @File : 063_爬虫_urllib_ajax的post请求
# @Project : python爬虫
# post

# 1页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# 2页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse


def create_request(page):
    base_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data = {
        "cname": "北京",
        "pageIndex": page,
        "pageSize": 10,
        "pid": ""
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(url=base_url, data=data, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    with open("kfc_" + str(page) + ".json", "a", encoding="utf-8") as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(page,content)
