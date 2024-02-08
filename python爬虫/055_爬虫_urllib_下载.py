# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 18:24
# Author : LeiZhuzheng
# @File : 055_爬虫_urllib_下载
# @Project : python爬虫

import urllib.request

# 下载一个网页
# url_page = "http://www.baidu.com"
# url :下载的路径  filename:文件的名字
# 在Python中  可以写变量的名字  也可以写值
# urllib.request.urlretrieve(url_page,"baidu.html")


# 下载图片
# url_img = "https://tse3-mm.cn.bing.net/th?id=OIF-C.1Esg1Os6As4OzD%2f4HUme1g&w=302&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
# urllib.request.urlretrieve(url=url_img, filename="lisa.jpg")

# 下载视频
url_video = "https://apd-vlive.apdcdn.tc.qq.com/vhot2.qqvideo.tc.qq.com/A5zOHlSk9SZ8_nr4rv0pUeL2Dey4aDO9YzYD652u6dCM/B_JxNyiJmktHRgresXhfyMejU9VSEeBNtjo45SdtTzr2KdVGrWo-p_R_5WmcY7cWpy/svp_50069/gzc_1000035_0b53s4bliaac6iahrvpzarsjpf6dwslqfnca.f622.mp4?sdtfrom=v1010&guid=f417711294b2f625&vkey=3F43D0ABA0FC47257A0375BA7B7DE3E732A2E056A84B5DA158E9CD0C94CAC2F69DCF656016F836522706C7701EB0B33E557291B0BC5DC8F49CF4C2425C8E2C76F22B20CBA54C11CF676A1308F0707C38C393F296F76BF72D7CD7CA328A2624D5E2C5C754BE53F6B4BEF0FB862A6B05E79BEC89E22A6500D38F63DBD57B1871EC425E5D924DB4B1C50C173566102286037362ADD0AD1DC29BF6CF87714EEC1D3BAD877B2DACA41A40"
urllib.request.urlretrieve(url=url_video, filename="lisa.mp4")
