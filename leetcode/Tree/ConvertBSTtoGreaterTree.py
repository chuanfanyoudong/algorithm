"""
给出一棵树，然后更新每个节点，每个节点的值都是加上所有比他大的值
容易看出用递归，root要加上root.right更新后的值，root.left要加上更新后的root的值
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
@author: zkjiang
@time: 2019/4/1 21:04
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        self.dfs(root, 0)
        return root

    def dfs(self, node, val):
        if node == None:
            return val
        # val为当前节点右节点的和
        val = self.dfs(node.right, val)
        node.val = node.val + val
        return self.dfs(node.left, node.val)
