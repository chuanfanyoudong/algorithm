"""
找出数组中第K大的值
用的是快拍的思路
@author: zkjiang
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
                right = partion
            if partion < len(nums) - k:
                left = partion + 1


    def helper(self, nums, left, right):
        # 作用就是返回的值k的意义为：第k个index的值右边的都比它大，左边的都比它小
        i = left + 1
        j = left + 1
        base = nums[left]
        while j < right:
            if nums[j] < base:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        nums[left], nums[i-1] = nums[i-1], nums[left]
        return i - 1

if __name__ == '__main__':
    tmp_list =  [7,6,5,4,3,2,1]
    k = 2
    print(Solution().findKthLargest(tmp_list,k))