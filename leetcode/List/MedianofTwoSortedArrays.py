"""
@time: 2019/3/28 22:16
"""

"""
找到两个数组的中值
初步看这个题目，想到如果长度和是奇数，就选择中间的那个，如果长度和是偶数，就选择中间的两个的平均数
分别设定两个标记，记录两个数组的idx，找到中间值就返回
注意不要超过数组长度
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 要不要特殊情况判断？
        # 设定两个idx
        tag = 0
        tags_1 = 0
        tags_2 = 0
        result_list = []
        length_1 = len(nums1)
        length_2 = len(nums2)
        all_length = length_1 + length_2
        result = all_length//2
        while tag != result+1:
            if tags_1 < length_1 and tags_2 < length_2:
                if nums1[tags_1] > nums2[tags_2]:
                    result_list.append(nums2[tags_2])
                    tags_2 += 1
                else:
                    result_list.append(nums1[tags_1])
                    tags_1 += 1
            elif tags_1 >= length_1:
                result_list.append(nums2[tags_2])
                tags_2 += 1
            elif tags_2 >= length_2:
                result_list.append(nums1[tags_1])
                tags_1 += 1
            tag += 1
        if all_length%2 == 1:
            return result_list[-1]
        else:
            return float(result_list[-1] + result_list[-2])/2


if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))


