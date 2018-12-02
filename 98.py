# -*- coding: utf-8 -*-
# @创建时间 : 3/12/2018 
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node,ma,mi):
            if not node:
                return True
            if node.val  >= ma or node.val <= mi:
                return False
            return helper(node.left,node.val,mi) and helper(node.right,ma,node.val)
        maxn = float("inf")
        minn = float("-inf")
        return helper(root,maxn,minn)