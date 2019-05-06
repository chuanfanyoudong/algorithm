"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: SpiralMatrix2.py
@time: 2019/2/23 21:53
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]

        right = n - 1
        left = 0
        up = 0
        down = n - 1
        # print(result)
        if n == 0:
            return result
        # i,j = 0,0
        start = 1
        while 1:
            for i in range(left, right + 1):
                fnal = result[up]
                fnal[i] = start
                start += 1
            up += 1
            if up > down:
                break
            for j in range(up, down + 1):
                result[j][right] = start
                start += 1
            right -= 1
            if left > right:
                break
            for z in range(right, left-1, -1):
                result[down][z] = start
                start += 1
            down -= 1
            if up > down:
                break
            for k in range(down, up-1, -1):
                result[k][left] = start
                start += 1
            left += 1
            if left > right:
                break
        return result



class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for i in range(n)]
        i = 1
        j = 1                                   # moving steps
        x = 0;y = -1                            # initial position
        flag = 0                                # control the direction
        dir = [[0,1],[1,0],[0,-1],[-1,0]]       # 4 directions(right,down,left,up)
        x_step,y_step = dir[flag]
        count = 2*n
        while i <= n**2:
            x += x_step                         # move to next position
            y += y_steps
            if j == count//2:                   # change the direction and initialize the moving steps
                j = 0
                flag = (flag+1)%4
                x_step,y_step = dir[flag]
                count -= 1
            res[x][y] = i
            i += 1
            j += 1
        return re

if __name__ == '__main__':
    print(Solution().generateMatrix(3))