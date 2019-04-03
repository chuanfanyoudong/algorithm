"""
给你一棵树和目标值，找出能得到和为目标值的路径
注意只能往下寻找，也就是说 只能5 3 3，不能5 10 -3
考虑用递归
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
@author: zkjiang
@time: 2019/4/3 22:52
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res=[0]
        # 先写一个函数来计算root开头的和为sum的个数
        def dfs(root,cursum):
            if not root:
                return
            if cursum-root.val==0:
                res[0]+=1
            if root.left:
                dfs(root.left,cursum-root.val)
            if root.right:
                dfs(root.right,cursum-root.val)
        if not root:
            return 0
        # 用一个栈结构，来记录所有的节点，当栈为空时，则说明遍历完了每个节点
        # 我们需要对每个节点进行一次上述函数的应用来维护总个数
        stack = [root]
        while stack:
            node = stack.pop()
            dfs(node,sum)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res[0]
