"""
经典题目，求解编辑距离
@author: zkjiang
@time: 2019/5/3 16:32
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        dp = [[0]*(n2 +1) for _ in range(n1+1)]
        # 注意第0行和第0列的值
        # 我一开始都设为0了，所以不行
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] )
                else:
                    # 1 + Math.min(Math.min(matrix[i - 1][j], matrix[i][j - 1]), matrix[i - 1][j - 1])
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1]+1, dp[i - 1][j - 1] + 1)
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"

    print(Solution().minDistance(word1, word2))