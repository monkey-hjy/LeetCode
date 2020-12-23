#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File    :   1324-竖直打印单词.py    
# @Author  :   Monkey
# @DATE    :   2020/12/23 上午11:40 


class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list = s.split(' ')
        result = []
        for index in range(max([len(i) for i in s_list])):
            r = ''
            for ss in s_list:
                try:
                    r += ss[index]
                except:
                    r += ' '
            result.append(r.rstrip(' '))
        return result


