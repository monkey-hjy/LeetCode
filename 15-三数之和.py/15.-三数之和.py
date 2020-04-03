# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 18:18
# @Author  : Monkey
# @File    : 15.-三数之和.py
# @Software: PyCharm
# @Demand  :
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

nums = [-1, 0, 1, 2, -1, -4]
result = set()
nums.sort()
for i in range(len(nums) - 2):
    left = i+1
    right = len(nums)-1
    while left < right:
        if nums[left] + nums[right] + nums[i] == 0:
            result.add((nums[i], nums[left], nums[right]))
            left += 1
            right -= 1
        elif nums[left] + nums[right] + nums[i] <= 0:
            left += 1
        else:
            right -= 1
print(list(result))
