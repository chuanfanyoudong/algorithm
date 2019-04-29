#!/usr/bin/env python 
# encoding: utf-8 

"""
@author: zkjiang
@description:
@site: https://www.github.com/chuanfanyoudong
@software: PyCharm
@file: NumberofIslands.py
@time: 2"0""1"9/4/29 "1"4:26
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return None
        row_num = len(grid)
        col_num = len(grid[0])
        visit = [["0"]*col_num for _ in range(row_num)]
        #这里需要做判断，记录哪些已经浏览过了，然后跳过，如果是"0"的也跳
        # 定义一个visit矩阵，记录这个位置有没有被浏览过
        res = 0
        for i in range(row_num):
            for j in range(col_num):
                if visit[i][j] == "0" and grid[i][j] == "1":
                    self.helper(i,j,visit, grid)
                    res += 1
        return res

    def helper(self, i, j, visit, grid):
        # 该函数的作用是找出一个点能连起来的岛屿
        visit[i][j] = "1"
        if i-1>=0:
            if grid[i-1][j] == "1" and visit[i-1][j] != "1":
                self.helper(i-1,j,visit,grid)
        if i + 1 < len(visit) :
            if grid[i + 1][j] == "1" and visit[i+1][j] != "1":
                self.helper(i+1,j,visit,grid)
        if j - 1>= 0:
            if grid[i][j-1] == "1"  and visit[i][j-1] != "1":
                self.helper(i,j-1, visit,grid)
        if j + 1 < len(visit[0]):
            if grid[i][j+1] == "1" and visit[i][j+1] != "1":
                self.helper(i, j+1, visit,grid)


if __name__ == '__main__':
    tmp_list = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(Solution().numIslands(tmp_list))