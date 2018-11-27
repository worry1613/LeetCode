# -*- coding: utf-8 -*-
# @创建时间 : 27/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/


import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        que = collections.deque()
        que.append(root)
        li = 0
        while que:
            level = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                level.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            if level:
                res.append(level if li % 2 == 0 else level[::-1])
            li += 1
        return res

