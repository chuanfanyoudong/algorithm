"""
递归爆内存，所以用迭代法
@author: zkjiang
@time: 2019/4/25 15:04
"""
import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
            """
        num = int(math.sqrt(n))
        result_list = [0]*(n+1)
        for i in range(1,num + 1):
            result_list[i*i] = 1
        num_list = [i*i for i in range(1,num + 1)]
        for i in range(2,n + 1):
            result_list[i] = min(result_list[i-j] + 1 for j in num_list if j <= i)
        return result_list[-1]


if __name__ == '__main__':
    n = 12
    print(Solution().numSquares(n))