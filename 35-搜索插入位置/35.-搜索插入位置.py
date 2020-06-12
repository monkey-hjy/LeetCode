# @Time : 2020/6/12 15:04 
# @Author : Monkey
# @Software: PyCharm


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 如果元素在列表中，则直接返回对应的下标
        if target in nums:
            return nums.index(target)
        # 如果元素不在列表中，则将这个元素加入列表，并进行排序，然后返回对应的下标
        else:
            nums.append(target)
            return sorted(nums).index(target)
