# 1.请求对象的定制
# 2.获取网页的源码
# 3.下载


# 需求 下载前10页的图片
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html

import urllib.request
from lxml import etree


def create_request(page):
    if (page == 1):
        url = "https://sc.chinaz.com/tupian/qinglvtupian.html"
    else:
        url = "https://sc.chinaz.com/tupian/qinglvtupian_" + str(page) + ".html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(content):
    # 下载图片
    # urllib.request.urlretrieve("图片地址", "文件名")
    tree = etree.HTML(content)
    name_list = tree.xpath(
        "//div[@class='tupian-list com-img-txt-list']/div[@class='item']/img/@alt")
    # 一般涉及图片的网站都会涉及懒加载
    src_list = tree.xpath(
        "//div[@class='tupian-list com-img-txt-list']/div[@class='item']/img/@data-original")
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = "https:" + src
        urllib.request.urlretrieve(url=url, filename="./072_love_imgs/" + name + ".png")


if __name__ == '__main__':
    start_page = int(input("请输入起始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page, end_page + 1):
        # 1.请求对象的定制
        request = create_request(page)
        # 2.获取网页源码
        content = get_content(request)
        # 3.下载
        down_load(content)
