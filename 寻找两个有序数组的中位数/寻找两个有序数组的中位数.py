# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 21:24
# @Author  : Monkey
# @File    : ClassCreate.py
# @Software: PyCharm
# @Demand  : 
'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

nums = sorted(nums1 + nums2)
if len(nums) % 2 == 0:
    # return float((nums[len(nums)//2-1] + nums[len(nums)//2]) / 2)
    print((nums[len(nums)//2-1] + nums[len(nums)//2]) / 2)
else:
    # return float(nums[len(nums) // 2])
    print(nums[len(nums) // 2])
