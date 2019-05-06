"""
判断两个矩阵是否重叠
就是找出重叠部分的坐标，判断这个点是不是存在
@author: zkjiang
@time: 2019/5/4 15:51
"""


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        new_left_x = max(rec1[0], rec2[0])
        new_left_y = max(rec1[1], rec2[1])
        new_right_x = min(rec1[2], rec2[2])
        new_right_y = min(rec1[3], rec2[3])
        if new_left_x < new_right_x and new_left_y < new_right_y:
            return True
        return False

if __name__ == '__main__':
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    print(Solution().isRectangleOverlap(rec1, rec2))

