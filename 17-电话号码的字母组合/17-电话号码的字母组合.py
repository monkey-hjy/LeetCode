# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 20:43
# @Author  : Monkey
# @File    : 17-电话号码的字母组合.py
# @Software: PyCharm
# @Demand  :
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''


class Solution:
    def letterCombinations(self, digits):
        key = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits == '':
            return []
        result = ['']
        for num in digits:
            result = [x + y for x in result for y in key[num]]
        return result


s = Solution
print(s.letterCombinations(s, '234'))

