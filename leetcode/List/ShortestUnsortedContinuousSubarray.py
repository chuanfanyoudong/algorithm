"""
给出一个数组，找出需要排序的部分，返回长度
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        这里可以有一个O(n)的方法，就是不断地更新start和end的位置，最后返回二者之差
        """
        if len(nums) < 2:
            return 0
        n = len(nums)
        max_num = nums[0]
        min_num = nums[-1]
        start, end = -1, -2
        for i in range(1, len(nums)):
            max_num = max(max_num, nums[i])
            if max_num > nums[i]:
                end = i
            min_num = min(min_num, nums[n - i - 1])
            if min_num < nums[ n - i - 1]:
                start = n-i-1
        return end - start + 1

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().findUnsortedSubarray(nums))

