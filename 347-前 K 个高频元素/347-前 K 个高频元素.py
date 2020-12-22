#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   347-前 K 个高频元素.py    
# @Author  :   Monkey
# @DATE    :   2020/12/22 下午4:08


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict()
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        need_count = sorted(num_dict.values(), reverse=True)[:k]
        result = [key for key in num_dict if num_dict[key] in need_count]
        return result



