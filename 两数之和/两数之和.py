# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 21:24
# @Author  : Monkey
# @File    : ClassCreate.py
# @Software: PyCharm
# @Demand  :
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
nums = [3, 3]
target = 6

for i in range(len(nums)):
    diff = target - nums[i]
    if diff in nums and nums.index(diff) != i:
        # return [i, nums.index(diff)]
        print(i, nums.index(diff))
