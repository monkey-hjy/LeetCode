# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 21:01
# @Author  : Monkey
# @File    : 18-四数之和.py
# @Software: PyCharm
# @Demand  :
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def fourSum(self, nums, target):
        result = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                k = j+1
                l = len(nums)-1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1

        return list(result)


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution.fourSum(Solution, nums, target))


