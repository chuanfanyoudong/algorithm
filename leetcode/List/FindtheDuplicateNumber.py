"""
这个题目可以用二分查找哦
@author: zkjiang
@time: 2019/4/25 11:08
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = min(nums)
        high = max(nums)
        while low < high:
            mid = (low + high)//2
            tag_res = 0
            for i in nums:
                if i <= mid:
                    tag_res += 1
            if tag_res <= mid:
                low = mid+1
            else:
                high = mid
        return low



if __name__ == '__main__':
    print(Solution().findDuplicate([1,3,4,2,2]))

