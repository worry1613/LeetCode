# -*- coding: utf-8 -*-
# @创建时间 : 2/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head