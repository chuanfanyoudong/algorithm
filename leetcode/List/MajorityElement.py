#!/usr/bin/env python 
# encoding: utf-8 

"""
@author: zkjiang
@description:
@site: https://www.github.com/chuanfanyoudong
@software: PyCharm
@file: MajorityElement.py
@time: 2019/4/30 8:41
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_num_dict = {}
        for i in nums:
            if i in max_num_dict:
                max_num_dict[i] += 1
            else:
                max_num_dict[i] = 1
            if max_num_dict[i] > n//2:
                return i
        result = sorted(max_num_dict.items(), key=lambda x:x[1], reverse=True)
        return result[0][0]



if __name__ == '__main__':
    tmp_list = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(tmp_list))
