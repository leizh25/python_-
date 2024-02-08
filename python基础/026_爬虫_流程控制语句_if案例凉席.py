# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 11:32
# Author : LeiZhuzheng
# @File : 026_爬虫_流程控制语句_if案例凉席
# @Project : python基础

# 在控制台上输入一个年龄 如果您的年龄大于18了 那么打印可以去网吧了
age = input("请输入您的年龄:")
# input 返回的是字符串类型
# print(type(age))

# 字符串和整形int是不可以比较的
if int(age) > 18:
    print("您可以去网吧了")
