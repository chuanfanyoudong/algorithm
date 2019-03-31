"""
@author: zkjiang
给出一个字符串，输出这个字符串所有的子串中是回文的那个
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 先做边界判断
        result = 0
        if s == "":
            return None
        if len(s) == 1:
            return s
        for i in range(len(s)):
            tag1 = 0
            tag2 = 0
            while i - tag1 >= 0 and i + tag1 + 1 <= len(s):
                if s[i-tag1:i+tag1+1] == s[i-tag1:i+tag1+1][::-1]:
                    # print(s[i-tag1:i+tag1+1])
                    result += 1
                else:
                    break
                tag1 += 1
            while i -tag2 >= 0 and i + tag2 + 2 <= len(s):
                if s[i-tag2:i+tag2+2] == s[i-tag2:i+tag2+2][::-1]:
                    # print(s[i-tag2:i+tag2+2])
                    result += 1
                else:
                    break
                tag2 += 1
        return result

if __name__ == '__main__':
    s = "aaaaa"
    print(Solution().countSubstrings(s))