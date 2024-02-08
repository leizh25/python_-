# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 17:35
# Author : LeiZhuzheng
# @File : 050_爬虫_异常
# @Project : python基础

# fp = open('aa.txt', 'w')
# fp.read()
# fp.close()

# # 异常的格式
# try:
# # 可能异常的代码
# except  # 异常的类型
# # 友好的提示


try:
    fp = open('aa.txt', 'r')
    fp.read()
except FileNotFoundError:
    print("系统正在升级,请稍后再试...")
