"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: CoinChange.py
@time: 2019/4/24 19:01
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp_list = [100000000] * (amount + 1)
        dp_list[0] = 0
        i = 1
        while i < amount + 1:
            for single_j in coins:
                if i - single_j >= 0:
                    dp_list[i] = min(dp_list[i], dp_list[i - single_j] + 1)
            i += 1
        if dp_list[-1] == 100000000:
            return -1
        return dp_list[-1]

if __name__ == '__main__':
    coins = [3]
    amount = 2
    print(Solution().coinChange(coins, amount))