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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxPath = [float('-inf')]
        def dfs(root,path):
            if not root: return 0
            l=max(0,dfs(root.left,path))
            r=max(0,dfs(root.right,path))
            path[0]=max(path[0],l+r+root.val)
            return root.val+max(l,r)
        dfs(root,maxPath)
        return maxPath[0]