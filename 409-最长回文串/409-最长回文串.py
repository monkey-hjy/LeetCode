#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   409-最长回文串.py    
# @Author  :   Monkey
# @DATE    :   2020/12/22 下午4:46 


class Solution:
    def longestPalindrome(self, s: str) -> int:
        return len(s) -max(0,sum([s.count(i)%2 for i in set(s)])-1)

