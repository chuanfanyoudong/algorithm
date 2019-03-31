"""
@author: zkjiang
返回一棵树是不是另一棵树的子树
递归吧，做一个函数这两棵树是不是相等，然后用或方法递归判断
@time: 2019/3/31 22:11
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None or t == None:
            return s == t
        else:
            # 这里判断两棵树相等或者s的左子树和t相等或者s的右子树和t相等
            return self.is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, s, t):
        """
        这个函数的作用是判断两棵树是否相等
        """
        if s == None or t == None:
            return s == t
        else:
            return s.val == t.val and self.is_same(s.left, t.left) and self.is_same(s.right, t.right)



