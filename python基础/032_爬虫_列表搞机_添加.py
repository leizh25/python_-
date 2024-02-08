# _*_ coding : utf-8 _*_
# @Time : 2024/2/7 12:29
# Author : LeiZhuzheng
# @File : 032_爬虫_列表搞机_添加
# @Project : python基础

# append  追加   在列表的最后来添加一个 对象 / 数据
food_list = ["铁锅炖大鹅", "酸菜五花肉"]
print(food_list)

food_list.append("小鸡炖蘑菇")
print(food_list)

# insert
char_list = ["a", "c", "d"]
print(char_list)
# index的值就是想要插入数据的下标
char_list.insert(1, "b")
print(char_list)

# extend  继承
num_list = [1, 2, 3]
num1_list = [4, 5, 6]
num_list.extend(num1_list)
print(num_list)
