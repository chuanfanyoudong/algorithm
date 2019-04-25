"""
给出一个数组，让你求出频率最高的K个
python中有Counter方法
@author: zkjiang
@time: 2019/4/5 19:40
"""
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_num = Counter(nums).most_common(k)
        return [i[0] for i in count_num]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))