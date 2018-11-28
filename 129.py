# -*- coding: utf-8 -*-
# @创建时间 : 28/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = []

        def dfs(root, c):
            if not root: return
            c = c * 10 + root.val
            if root.left: dfs(root.left, c)
            if root.right: dfs(root.right, c)
            if not root.left and not root.right: count.append(c)

        dfs(root, 0)
        return sum(count)