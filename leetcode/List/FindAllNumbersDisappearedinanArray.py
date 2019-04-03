"""
找出数组长度为n找出1-n的数不出现在数组中的值
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

@author: zkjiang
@time: 2019/4/2 21:36
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        该方法不会超时
        """
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        return [i+1 for i,num in enumerate(nums) if num > 0]


    def findDisappearedNumbers1(self, nums):
        """
        下面的方法会超时，所以不能这么做
        """
        if len(nums) == 0:
            return []
        result = []
        n = len(nums)
        for i in range(1,n+1):
            if i not in nums:
                result.append(i)
        return result
