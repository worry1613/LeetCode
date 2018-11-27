# -*- coding: utf-8 -*-
# @创建时间 : 27/11/2018 
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return
        root = TreeNode(preorder[0])
        n = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:n + 1], inorder[:n])
        root.right = self.buildTree(preorder[n + 1:], inorder[n + 1:])
        return root

