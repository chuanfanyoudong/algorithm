"""
输入一个数组，和一个目标和，然后用+，-号拼出目标值
考虑用递归
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
@author: zkjiang
@time: 2019/4/2 20:19
"""
import collections


class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        递归超时，则用迭代方法，做一个字典分别更新从头遍历的每次和的情况
        所以动态规划搞起来，之前自己写错了，看了别人的答案，知道要维护一个数组，每个元素是一个字典
        每个字典记录了当前位置所有可能的和
        """
        _len = len(nums)
        dp = [collections.defaultdict(int) for _ in range(_len + 1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, count in dp[i].items():
                dp[i+1][sum + num] += count
                dp[i+1][sum - num] += count
        if S in dp[_len]:
            return dp[_len][S]
        return 0



    # result = 0
    # def findTargetSumWays1(self, nums, S):
    #     """
    #     这是递归方法，但是leetcode会超时
    #     注意的一点就是当nums的长度为1时候，且等于S则加1
    #     """
    #     if len(nums) == 1:
    #         #这里注意以为第一个字符前面可以加负号，所以可以有两种情况
    #         if nums[0] == S:
    #             self.result += 1
    #         if nums[0] == -S:
    #             self.result += 1
    #     else:
    #         target = nums[0]
    #         self.findTargetSumWays(nums[1:], S - target)
    #         self.findTargetSumWays(nums[1:], S + target)
    #     return self.result



if __name__ == '__main__':
    nums = [1,1,1,1,1]
    S = 3
    print(Solution().findTargetSumWays(nums, S))