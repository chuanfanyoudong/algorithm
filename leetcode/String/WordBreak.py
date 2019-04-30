"""
不要用递归，用动态规划
@author: zkjiang
@time: 2019/4/30 20:38
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        result_lis = [0]*(n+1)
        for i in range(n+1):
            for k in range(i):
                if (result_lis[k] and s[k:i] in wordDict) or s[:i] in wordDict:
                    result_lis[i] = 1
                    # break
        return result_lis[-1]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))


