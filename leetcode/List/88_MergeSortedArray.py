"""
排序两个数组
就是找到最大的值放在最后面
@author: zkjiang
@time: 2019/5/4 7:37
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = m + n
        while m > 0 and n > 0:
            if nums2[n-1] > nums1[m-1]:
                nums1[k-1] = nums2[n-1]
                n -= 1
            else:
                nums1[k-1] = nums1[m-1]
                m -= 1
            k -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1

if __name__ == '__main__':
    nums1 = [8, 9, 0, 0, 0, 0]
    m = 2
    nums2 = [4, 5, 6,7]
    n = 4
    print(Solution().merge(nums1, m, nums2, n))
