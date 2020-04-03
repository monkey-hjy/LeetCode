# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 21:25
# @Author  : Monkey
# @File    : 20-有效的括号.py
# @Software: PyCharm
# @Demand  :
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isValid(self, s: str):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')
        return s == ''


print(Solution.isValid(Solution, '{()}()[]'))


