"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: Searcha2DMatrix2.py
@time: 2019/4/25 16:54
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        row_num = len(matrix)
        col_num = len(matrix[0])
        i = row_num - 1
        j = 0
        while i >= 0 and j < col_num:
            if matrix[i][j] == target:
                return 1
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
        return False
if __name__ == '__main__':

    tmp_list = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    print(Solution().searchMatrix(tmp_list, 1000))