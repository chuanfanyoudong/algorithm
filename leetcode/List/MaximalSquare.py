"""
总结动态规划公式
@author: zkjiang
@time: 2019/4/26 1:02
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        dp = matrix
        m = len(matrix)
        n = len(matrix[0])
        # res = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(int(dp[i-1][j]), int(dp[i][j-1]), int(dp[i-1][j-1])) + 1
                    # res = max(dp[i][j], res)
                else:
                    dp[i][j] = 0
        res = 0
        for i in matrix:
            for j in i:
                res = max(int(j), res)
        return res*res


if __name__ == '__main__':
    print(Solution().maximalSquare( [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))