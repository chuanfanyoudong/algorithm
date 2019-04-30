#!/usr/bin/env python 
# encoding: utf-8 

"""
@author: zkjiang
@description:
@site: https://www.github.com/chuanfanyoudong
@software: PyCharm
@file: HouseRobber.py
@time: 2019/4/30 8:27
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        max_num = [0] * len(nums)
        max_num[0] = nums[0]
        max_num[1] = max(nums[0], nums[1])
        for i in range(2, n):
            max_num[i] = max(max_num[i-1], max_num[i-2] + nums[i])
        return max_num[-1]