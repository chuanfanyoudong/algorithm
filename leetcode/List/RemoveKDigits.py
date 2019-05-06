"""
删除序列的K个元素，使得该序列具有最小的值
注意为0的情况，维护一个栈，到最后取出前n-k个元素
如果新的元素进来，并且比前面的元素小，就把前面的元素干掉
@author: zkjiang
@time: 2019/5/1 9:35
"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        k_origin = k
        stack = [int(num[0])]
        i = 1
        while i < n:
            while stack != [] and int(num[i]) < stack[-1] and k > 0 :
                stack.pop()
                k -= 1
            stack.append(int(num[i]))
            i += 1
        result = stack[:len(num)-k_origin]
        while result != [] and result[0] == 0:
            result.pop(0)
        if result == []:
            return "0"
        else:
            return "".join([str(i) for i in result])

if __name__ == '__main__':
    num = "1234567890"
    k = 9
    # k = 2
    print(Solution().removeKdigits(num, k))
