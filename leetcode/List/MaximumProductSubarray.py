#!/usr/bin/env python 
# encoding: utf-8 

"""
@author: zkjiang
求一个数组的最大乘积字串，考虑正负情况，这个问题的思路就是维护两个数组，一个最大值数组，一个最小值数组
@time: 2019/4/30 9:05
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        max_list = [0]*n
        max_list[0] = nums[0]
        min_list = [0]*n
        min_list[0] = nums[0]
        max_result = nums[0]
        for i in range(1,n):
            max_list[i] = max(max_list[i-1]*nums[i], min_list[i-1]*nums[i], nums[i])
            min_list[i] = min(max_list[i-1]*nums[i], min_list[i-1]*nums[i], nums[i])
            max_result = max(max_result, max_list[i])
        return max_result


if __name__ == '__main__':
    tmp_list = [2, 3, -2, 4]
    print(Solution().maxProduct(tmp_list))

