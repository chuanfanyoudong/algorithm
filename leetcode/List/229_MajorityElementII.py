"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: 229_MajorityElementII.py
@time: 2019/5/4 16:06
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return None
        if len(nums) == 1:
            return nums[0]
        count1 = 0
        count2 = 0
        res1 = 0
        res2 = 0
        for i in nums:
            if count1 == 0:
                res1 = i
                count1 += 1
            elif i == res1:
                count1 += 1
            elif count2 == 0:
                res2 = i
                count2 += 1
            elif i == res2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        return [res1, res2]


if __name__ == '__main__':
    tmp_list = [1,1,1,3,3,2,2,2]
    print(Solution().majorityElement(tmp_list))