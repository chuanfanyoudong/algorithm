"""
给你一个数组，看是不是这个数组可以分成两个和相等的子数组
@author: zkjiang
@time: 2019/4/4 0:25
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return 0
        nums_sum = sum(nums)
        if nums%2 == 1:
            return 0
        nums = sorted(nums)
        nums_sum_final = nums_sum/2
        i,j = 0, 1
        while j < len(nums):
            if nums[i:j] =

