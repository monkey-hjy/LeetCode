#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   830-较大分组的位置.py    
# @Author  :   Monkey
# @DATE    :   2020/12/22 下午5:10 


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        index = 0
        result = []
        while index < len(s)-1:
            count = 0
            for j in range(index+1, len(s)):
                if s[j] != s[index]:
                    break
                count += 1
                index += 1
            if count == 0:
                index += 1
            if count >= 2:
                result.append([index-count, index])
        return result



