"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: 151_ReverseWordsinaString.py
@time: 2019/5/3 18:35
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in range(len(s)):
            if s[i] == "":
                start = i + 1
            elif i == len(s)-1:
                print(s[start:i+1])
            elif s[i+1] == "":
                print(s[start:i])



if __name__ == '__main__':
    tmp_str = "a good   example"
    print(Solution().reverseWords(tmp_str))