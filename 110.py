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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        #         def maxDepth(node):
        #             if not node:#递归边界
        #                 return 0
        #             else:
        #                 return max(maxDepth(node.left),maxDepth(node.right))+1

        #         if not root:#递归边界
        #             return True
        #         else:
        #             l,r = 0,0
        #             if root.left: l=maxDepth(root.left)#递归
        #             if root.right: r=maxDepth(root.right)
        #             # return l,r
        #             return False if abs(l-r) >1 else True
        def height(node):
            if node == None:
                return 0
            else:
                return max(height(node.left), height(node.right)) + 1

        if root == None:
            return True
        elif abs(height(root.left) - height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
