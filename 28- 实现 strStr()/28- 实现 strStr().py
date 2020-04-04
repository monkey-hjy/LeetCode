# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 15:08
# @Author  : Monkey
# @File    : 28- 实现 strStr().py
# @Software: PyCharm
# @Demand  :
'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                print(haystack[i:len(needle)])
                return i
        return -1


print(Solution.strStr(Solution, 'hello', 'll'))

