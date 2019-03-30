"""
@time: 2019/3/28 21:33
"""

"""
找一个字符串的最长的不重复的子串
目前我想到的就是做了两个标记start，end
开始start, end = 0，max = 0
然后end开始加，如果发现end的值和start一样,start+1否则不变，那么只需要每次更新max就好了
但是这个思路有问题，因为你没法保证新发现的char有可能和start位置的重复，也有可能和其他重复
所以看网上，需要用一个字典来记录当前非重复子串的每个值的位置，这样就没问题了
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 特殊情况判断
        if len(s) < 2:
            return len(s)
        # 设置上述的三个参数
        str_dict = {}
        start = max_length = 0
        end = 0
        while end < len(s):
            # 这个更新start值的坐标条件很重要，并不是s【end】不字典里就要更新，并且需要这个字在字典里的idx（value值）要大于start
            if s[end] in str_dict and str_dict[s[end]] >= start:
                start = str_dict[s[end]] + 1
            # 无论什么情况，都要更新是s[end]的值
            str_dict[s[end]] = end
            # 都要更新最大值
            max_length = max(end-start+1, max_length)
            end += 1
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
