# -*- coding: utf-8 -*-
# @创建时间 : 10/12/2018 
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []

        def dfs(node, path):
            if not node.left and not node.right:
                ret.append(path + str(node.val))
                return
            if node.left: dfs(node.left, path + str(node.val) + '->')
            if node.right: dfs(node.right, path + str(node.val) + '->')

        if not root: return []
        dfs(root, '')
        return ret
