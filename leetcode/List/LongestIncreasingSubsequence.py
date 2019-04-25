"""
求一个数组的最大递增数组的长度，
解决方法就是维护一个数组记录仪i结尾时的最大长度，
对第i个值，分别和前面的结果比较，如果他比前面index位置上的值大，则位置i的最大长度为index的最大长度加一
@author: zkjiang
@time: 2019/4/25 0:34
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        n = len(nums)
        result_list = [1]*n
        for i in range(1,n):
            max_length = -1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_length = max(max_length, result_list[j] + 1)
                if max_length == -1:
                    result_list[i] = 1
                else:
                    result_list[i] = max_length
        return max(result_list)




if __name__ == '__main__':
    tmp_list= [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(tmp_list))