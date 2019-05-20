# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    level = 0
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        stack = []
        max_level = 0
        node = pRoot
        while node or stack:
            if node:
                stack.append([pRoot, self.level])
                node = node.left
                self.level += 1
            else:
                node, tmp_level = stack.pop()
                max_level = max(max_level, tmp_level)
                node = node.right
                self.level = tmp_level + 1
        return max_level
                
                
                
                
            
            