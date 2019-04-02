"""
求一棵树的直径，也就是所有两个节点的最远距离的最大值，注意这个值不一定非要通过root
考虑用递归，递归计算每个节点的深度，然后该节点为最上层点时候的直径就是该节点的左子节点的深度
加上右子节点的深度
@author: zkjiang
@time: 2019/4/1 20:14
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        # 如果root为None则返回0
        if not root: return 0
        # 特殊情况判断，如果root没有左右子节点，则返回0
        if root.left == None and root.right == None:
            return 0
        # 求树的深度函数
        # 相当于在求深度的过程中更新了直径的值
        # 在求每一个节点深度的时候
        self.cal_depth(root)
        return self.diameter

    def cal_depth(self, node):

        if not node:
            return 0
        if not node.right and not node.left:
            return 1
        leftDiameter = self.cal_depth(node.left)
        rightDiameter = self.cal_depth(node.right)
        if leftDiameter + rightDiameter > self.diameter:
            self.diameter = leftDiameter + rightDiameter
        # 当前节点的深度等于左右深度最大值 + 1
        return max(leftDiameter, rightDiameter) + 1


