# -*- coding: utf-8 -*-
# @创建时间 : 27/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isOK(root.left, root.right)
    def isOK(self,left,right):
        if not left and not right: return True
        if not left: return False
        if not right: return False
        if left.val != right.val: return False
        return self.isOK(left.left,right.right) and self.isOK(left.right,right.left)

