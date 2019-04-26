"""
做两个序列，一个代表着这个数字之前所有数字的乘积
另一个代表着这个数字之后所有数字的乘积
@author: zkjiang
@time: 2019/4/25 17:13
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1 or len(nums) == 0:
            return nums
        n = len(nums)
        forward_list = [1]*n
        backward_list = [1]*n
        f = 1
        for i in range(1,n):
            f = f*nums[i-1]
            forward_list[i] = f
        print(forward_list)
        b = 1
        for i in range(n-2,-1,-1):
            b = b*nums[i+1]
            backward_list[i] = b*forward_list[i]
        backward_list[n-1] = forward_list[n-1]
        return backward_list





if __name__ == '__main__':
    tmp_list =  [1,2,3,4]
    print(Solution().productExceptSelf(tmp_list))
