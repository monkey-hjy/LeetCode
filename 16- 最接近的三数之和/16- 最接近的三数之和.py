# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 20:16
# @Author  : Monkey
# @File    : 16- 最接近的三数之和.py
# @Software: PyCharm
# @Demand  :
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def threeSumClosest(nums, target):
    diff = abs(nums[0] + nums[1] + nums[2] - target)
    result = nums[0] + nums[1] + nums[2]
    if diff == 0:
        return target
    nums.sort()
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j < k:
            print(diff, result, i, j, k)
            if nums[i] + nums[j] + nums[k] == target:
                return target
            elif abs(nums[i] + nums[j] + nums[k] - target) < diff:
                diff = abs(nums[i] + nums[j] + nums[k] - target)
                result = nums[i] + nums[j] + nums[k]
            if nums[i] + nums[j] + nums[k] < target:
                j += 1
            else:
                k -= 1

    return result


nums = [-3,-2,-5,3,-4]
target = -1
print(threeSumClosest(nums, target))

