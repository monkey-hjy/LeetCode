# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 17:33
# @Author  : Monkey
# @File    : 14-最长公共前缀.py
# @Software: PyCharm
# @Demand  :
'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
'''

strs = []
# 如果不是空列表，则进行计算
if len(strs) != 0:
    s_l = []
    # 求出来每一个字符的长度
    for i in range(len(strs)):
        s_l.append(len(strs[i]))
    b = True
    # 求出最短元素的下标
    index = s_l.index(min(s_l))
    # 将最短的元素设置为结果
    result = strs[index]
    # 遍历结果
    for i in range(len(result)):
        # 遍历列表。进行判断前缀是否相同
        for j in range(len(strs)):
            # 如果遇到不相同的前缀，则结束循环
            if strs[j][i] != result[i]:
                b = False
                break
        if not b:
            result = result[:i]
            break
    # return result
    print(result)
else:
    # return ''
    print(strs)

