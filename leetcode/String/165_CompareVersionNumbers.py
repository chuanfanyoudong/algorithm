"""
比较两个版本号的大小
注意001和00001是一样的
注意各种细节
@author: zkjiang
@time: 2019/5/3 20:46
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = version1.split(".")
        v2_list = version2.split(".")
        for i in range(len(v1_list)):
            v1_list[i] = self.simply(v1_list[i])
        for i in range(len(v2_list)):
            v2_list[i] = self.simply(v2_list[i])
        n1 = len(v1_list)
        n2 = len(v2_list)
        n = max(n1, n2)
        for i in range(n):
            if i < n1:
                v1_num = int(v1_list[i])
            else:
                v1_num = 0
            if i < n2:
                v2_num = int(v2_list[i])
            else:
                v2_num = 0
            if v1_num > v2_num:
                return 1
            if v1_num < v2_num:
                return -1
        return 0


    def simply(self, target_str):
        i = 0
        n = len(target_str)
        if n == 1:
            return target_str
        while i < n-1:
            if target_str[i] == "0":
                i += 1
            else:
                break
        return target_str[i:]


if __name__ == '__main__':
    version1 = "1.0"
    version2 = "1"
    print(Solution().compareVersion(version1, version2))