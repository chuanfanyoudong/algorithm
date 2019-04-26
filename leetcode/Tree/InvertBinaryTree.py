"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: InvertBinaryTree.py
@time: 2019/4/26 0:12
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        quene = [root]
        while quene:
            node = quene.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                quene.append(node.left)
                quene.append(node.right)
        return root
    # recursively
    def invertTree1(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

    # BFS
    def invertTree2(self, root):
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

    # DFS
    def invertTree3(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root