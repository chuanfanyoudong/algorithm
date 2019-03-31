
"""
J代表是宝石的str就是是说J中的每一个元素都是宝石，S是一个字符串，问S中有多少个宝石
例：
Input: J = "aA", S = "aAAbbbb"
Output: 3
S 中有一个a两个A所以共有三个宝石
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        这个比较简单，先做特殊情况判断，然后遍历S依次判断是否在J中
        """
        result = 0
        # 特殊情况判断
        if J == "" or S == "":
            return 0
        # 遍历S
        for i in S:
            # 如果S中的某个元素在J中
            if i in J:
                # 结果加1
                result += 1
        return result