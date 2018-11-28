# -*- coding: utf-8 -*-
# @创建时间 : 28/11/2018 
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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 前序遍历，保存结点进list，遍历list重建树
        ans = []
        def preOrderTravel(root):
            if not root: return
            ans.append(root)
            preOrderTravel(root.left)
            preOrderTravel(root.right)
        preOrderTravel(root)
        copy = root
        for i in range(1, len(ans)):
            copy.left = None
            copy.right = ans[i]
            copy = ans[i]