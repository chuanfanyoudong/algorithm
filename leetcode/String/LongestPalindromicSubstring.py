"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: LongestPalindromicSubstring.py
@time: 2019/3/30 23:59
"""
"""
找到一个字符串的最长的回文
该问题可以有n2、n两种方法
"""


class Solution1(object):
    def longestPalindrome(self, s):
        """
        先自己写一个n2方法，主要就是遍历每一个值，找到每一个值为中点的回文最大长度（要注意奇数和偶数，奇数的话当前值为中点，偶数的和娿
        当前值和下一个值为中间两个）
        但是测试的时候显示超时，所以只能改进方法
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        if len(s) == 1:
            return s
        # 遍历s中的每一个值
        max_str = ""
        for i in range(len(s)):
            # 下面是依次判断奇数和偶数的最大回文
            # 为奇数时
            tag1 = 0
            tag2 = 0
            while i-tag1 >= 0 and i + tag1 + 1 <= len(s):
                if s[i-tag1:i+tag1+1] == s[i-tag1:i+tag1+1][::-1]:
                    if len(s[i-tag1:i+tag1+1]) > len(max_str):
                        max_str = s[i-tag1:i+tag1+1]
                tag1 += 1
            # 为偶数时，这个要注意i+tag1的最大值
            while i - tag2 >= 0 and i + tag2 + 2 <= len(s):
                if s[i-tag2:i+tag2+2] == s[i-tag2:i+tag2+2][::-1]:
                    if len(s[i-tag2:i+tag2+2]) > len(max_str):
                        max_str = s[i-tag2:i+tag2+2]
                tag2 += 1
        return max_str


class Solution:
    # 这里就是n的方法，这有点难以理解
    # 链接：https://blog.csdn.net/u013309870/article/details/70742315

    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        # 首先用“#”对s填充
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        # 设计一个参数，记录每一个位置的最大回文长度
        # Len[i] - 1即为以i为中心的最长回文子串在S中的长度。
        # 在S_new中，以S_new[i]为中心的最长回文子串长度为2Len[i] - 1，
        # 由于在S_new中是在每个字符两侧都有新字符“#”，观察可知“#”的数量一定是比原字符多1的，
        # 即有Len[i]个，因此真实的回文子串长度为Len[i] - 1，最长回文子串长度为Math.max(Len) - 1。
        P = [0] * n
        # 这个记录最大值的中心和最右边的位置
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # 这里就是给P【i】的默认值，
            # 就是如果i超过了R，那么P【i】就一定是0
            # 如果没超过，那么P【i】就是i关于c对称位置的p【i'】的值，但是如果p【i'】越界，超过了C的范围
            # 那么也是不行的，只有在C的范围里面，才能扩展P【i】的值
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        # 根据最大长度idx求出左右两个位置的id
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]

if __name__ == '__main__':
    s = "ababb"
    print(Solution().longestPalindrome(s))


