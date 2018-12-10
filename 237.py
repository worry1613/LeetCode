# -*- coding: utf-8 -*-
# @创建时间 : 10/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        没明白什么意思
        """
        if node == None: return node
        if node.next == None:
            node = None
        node.val = node.next.val
        node.next = node.next.next
