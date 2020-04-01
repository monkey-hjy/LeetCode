# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 21:24
# @Author  : Monkey
# @File    : ClassCreate.py
# @Software: PyCharm
# @Demand  : 
'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
'''

List = [1, 2]
max_area = 0
left = 0
right = len(List) - 1
while left < right:
    width = right - left
    if List[left] < List[right]:
        height = List[left]
        left += 1
    else:
        height = List[right]
        right -= 1
    if width * height > max_area:
        max_area = width * height

print(max_area)
