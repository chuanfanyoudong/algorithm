"""
维护两个表，分别记录最低的几个，和最高的利润
@author: zkjiang
@time: 2019/4/30 19:38
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1 or n == 0:
            return 0
        min_price = [0] * n
        min_price[0] = prices[0]
        min_pri = prices[0]
        max_profit = [0] * n
        for i in range(1,n):
            min_pri =  min(min_pri, prices[i])
            min_price[i] = min_pri
            max_profit[i] = max(0, prices[i] - min_price[i-1])
        return max(max_profit)


if __name__ == '__main__':
    tmp_list = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(tmp_list))





