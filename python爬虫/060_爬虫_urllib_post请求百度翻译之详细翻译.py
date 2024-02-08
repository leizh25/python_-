# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 21:20
# Author : LeiZhuzheng
# @File : 060_爬虫_urllib_post请求百度翻译之详细翻译
# @Project : python爬虫

import urllib.request
import urllib.parse
import  json
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
    "Cookie":"BAIDUID_BFESS=A331443933438A8A2245C42AFB0F6110:FG=1; H_WISE_SIDS=39647_39671_39676_39712_39738_39779_39790_39787_39703_39683_39678_39817_39664_39841; BIDUPSID=A331443933438A8A2245C42AFB0F6110; PSTM=1707022393; H_PS_PSSID=40155_39996_40010_40171_40203_39662_40207_40212_40217_40224; ZFY=gxSnrEjh5oNZ61qVQCcwth5ZCIeRKfLHCoo5BlrRvss:C; H_WISE_SIDS_BFESS=39647_39671_39676_39712_39738_39779_39790_39787_39703_39683_39678_39817_39664_39841; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1707312051; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1707312051; APPGUIDE_10_6_9=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_ZTNjNjhlMjg4MzU2ZWM0MzU0OWJhMzliZmI4NjA2YTgxNDJiMWMwMDE1MTcwYWMyODkyMjY4MjUxZWNkMDNjNzI4YWMwMWIxYzg4NzU5ZDM1NmZmOWE5Y2I4MjlkMDYxMDFhZmIyNzI4NWNlYmY1YzkzNDk1NTAwZDhiYWMwMzc3YWI3NDVjYTJmMzc2NTYyOGUzYjdhMmY1NGUyNTA0Ng==",
}

data = {
    "from": "en",
    "to": "zh",
    "query": "spider",
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "63766.268839",
    "token": "da29ca9c2769a540d22b0b0b6816862d",
    "domain": "common",
    "ts": "1707312057926"
}
# post 请求的参数必须进行编码 并且调用encode方法
data = urllib.parse.urlencode(data).encode("utf-8")

# 请求对象的定制
request = urllib.request.Request(url, data, headers)

# 模拟浏览器请求
response = urllib.request.urlopen(request)

# 读取内容
content = response.read().decode("utf-8")

obj = json.loads(content)
print(obj)
