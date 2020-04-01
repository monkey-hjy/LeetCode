# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 21:24
# @Author  : Monkey
# @File    : ClassCreate.py
# @Software: PyCharm
# @Demand  :
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer/
'''
x = '123'
a = str(x)
if a[0] == '-':
    b = '-'
    b += a[len(a):0:-1]
else:
    b = ''
    b += a[::-1]
if -2**31<=int(b)<=2**31-1:
    # return int(b)
    print(int(b))
else:
    # return 0
    print(0)
