#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   566-重塑矩阵.py    
# @Author  :   Monkey
# @DATE    :   2020/12/22 下午5:19 


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        new_nums = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
        if r*c != len(new_nums):
            return nums
        result = []
        for i in range(r):
            result.append(new_nums[i*c: (i+1)*c])
        return result

