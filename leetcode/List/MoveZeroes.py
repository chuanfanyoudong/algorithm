"""
@author: zkjiang
@time: 2019/4/25 11:57
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
        return nums

if __name__ == '__main__':
    print(Solution().moveZeroes(
[0,1,0,3,12]))
    [0, 1, 0, 3, 12]