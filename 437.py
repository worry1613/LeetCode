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
import collections


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        d[0] = 1

        def pSum(root, cur, sum):
            if not root: return 0
            res = 0
            cur += root.val
            if cur - sum in d:
                res += d[cur - sum]
            d[cur] += 1
            res += pSum(root.left, cur, sum) + pSum(root.right, cur, sum)
            d[cur] -= 1
            return res

        return pSum(root, 0, sum)

    #     if root == None:
    #         return 0
    #     else:
    #         return self.pathForm(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    # def pathForm(self, root, val):
    #     if root == None:
    #         return 0
    #     return 1 if root.val == val else 0 +self.pathForm(root.left, val - root.val) + self.pathForm(root.right, val - root.val)


