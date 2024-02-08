# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 14:45
# Author : LeiZhuzheng
# @File : 034_爬虫_列表高级_查询
# @Project : python基础

# in 判断某一个元素是否在某一个列表中
# food_list = ['香蕉', '苹果', '橘子', '橙子', '火龙果', '椰子']
# # 判断一下控制台输入的那个数据  是否在列表中
# food = input('请输入要查询的水果：')
# if food in food_list:
#     print('水果在列表中')
# else:
#     print('水果不在')

# not in 判断一个元素
ball_list = ['足球', '篮球', '排球', '棒球']
# 在控制台输入你喜欢的球类  判断是否不在这个列表中
ball = input('请输入你喜欢的球类：')
if ball not in ball_list:
    print('你所喜欢的球类不在我们的列表中')
else:
    print('你所喜欢的球类在我们的列表中')
