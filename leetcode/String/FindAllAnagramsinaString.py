"""
找出s中的所有的p或者p的换顺序后的结果
这题有点儿难，用滑窗做，就是永远在维护一个长度为len（p）的滑窗，
然后维护一个count值，当count值变成0的时候，说明这个滑窗是没问题的。
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

@author: zkjiang
@time: 2019/4/2 22:13
"""

class Solution(object):
    def findAnagrams(self, s, p):
        from collections import defaultdict
        begin, end = 0, 0
        count = len(p)
        ans = []
        d = defaultdict(int)
        for i in p:
            d[i] += 1
        while end < len(s):
            # 如果加进来的值不在p里面，那么count的值就不减1
            if d[s[end]] > 0:
                count -= 1
            # 这里的-= 1是为了与后面的d[s[begin]] += 1 相对应
            d[s[end]] -= 1
            end += 1
            #匹配成功
            if count == 0:
                ans.append(begin)
            #字串长度和p相等，begin向前移动
            if end - begin == len(p):
                #begin向前移动
                # 这边说明向前移动窗口了，那么说明s[begin]在字典中的值+1
                d[s[begin]] += 1
                begin += 1
                #加1后>=1，说明子串还需要begin对应的字符，即begin抛弃的字符还有用我们需要在后面补上。
                if d[s[begin-1]] >= 1:
                    count += 1
        return ans

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s,p))