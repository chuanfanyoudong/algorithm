"""
给你一个数组，看是不是这个数组可以分成两个和相等的子数组
想到这个题可以用动态规划求解
dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i]]
其中i为数组的坐标+1，j为目标值，有了这个迭代公式，就可以做了
然后动态规划一定要把初始值做好
当i == 0 时，dp[0][j] == 0
当j == 0 时，dp[i][0] == 1
@author: zkjiang
@time: 2019/4/4 0:25
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return 0
        nums_sum = sum(nums)
        N = len(nums)
        if nums_sum%2 == 1:
            return 0
        nums = sorted(nums)
        nums_sum_final = nums_sum//2
        dp = [[0]*(nums_sum_final + 1) for _ in range(N + 1)]
        for j in range(nums_sum_final + 1):
            dp[0][j] = 0
        for i in range(N + 1):
            dp[i][0] = 1
        for i in range(1, N + 1):
            for j in range(1, nums_sum_final + 1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i - 1][j]|dp[i - 1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[N][nums_sum_final]


if __name__ == '__main__':
    test_list = [1, 5, 7, 5]
    print(Solution().canPartition(test_list))