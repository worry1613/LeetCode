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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.total = sum

        # def caculate(root,sum,templist):
        #     if not root:
        #         return
        #     if not root.left and not root.right:
        #         if root.val+sum == self.total:
        #             self.res.append(templist+[root.val])
        #     if root.left:
        #         caculate(root.left,sum+root.val,templist+[root.val])
        #     if root.right:
        #         caculate(root.right,sum+root.val,templist+[root.val])
        # caculate(root,0,[])
        def caculate(root, sum, templist):
            if not root: return
            if not root.left and not root.right:
                if sum - root.val == 0: self.res.append(templist + [root.val])
            if root.left:
                caculate(root.left, sum - root.val, templist + [root.val])
            if root.right:
                caculate(root.right, sum - root.val, templist + [root.val])

        caculate(root, sum, [])
        return self.res

