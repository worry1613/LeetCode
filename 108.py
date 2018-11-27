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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #         def makeTree(num,start,end):
        #             if start>end:
        #                 return None

        #             mid=start+(end-start)//2
        #             node=TreeNode(num[mid])
        #             node.left=makeTree(num,start,mid-1)
        #             node.right=makeTree(num,mid+1,end)
        #             return node

        #         if len(num)==0:
        #             return None
        #         return makeTree(num,0,len(num)-1)
        if not nums:
            return None
        mean = len(nums) // 2
        tree = TreeNode(nums[mean])
        tree.left = self.sortedArrayToBST(nums[:mean])
        tree.right = self.sortedArrayToBST(nums[mean + 1:])
        return tree