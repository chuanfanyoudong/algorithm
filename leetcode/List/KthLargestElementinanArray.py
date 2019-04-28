"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: KthLargestElementinanArray.py
@time: 2019/4/29 6:55
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 and k == 1:
            return nums[0]
        left = 0
        right = len(nums)

        while 1:
            partion = self.helper(nums, left, right)
            # 这说明数列中index为2的的位置的值是第right - partion大的值
            if partion == len(nums) - k:
                return nums[partion]
            if partion > len(nums) - k:
                # 说明超过了，也就是
                right = right - partion
            if partion < len(nums) - k:
                left = partion + 1


    def helper(self, nums, left, right):
        i = left
        j = left
        base = nums[left]
        while j < right:
            if nums[j] < base:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        return i

if __name__ == '__main__':
    tmp_list =  [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(tmp_list,k))