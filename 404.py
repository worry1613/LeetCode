# -*- coding: utf-8 -*-
# @创建时间 : 15/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        n = 0
        if not root: return n
        if root.left and not root.left.left and not root.left.right:
            n += root.left.val
        n += self.sumOfLeftLeaves(root.left)
        n += self.sumOfLeftLeaves(root.right)
        return n
