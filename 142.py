# -*- coding: utf-8 -*-
# @创建时间 : 3/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return
        if not head.next: return
        f = head
        s = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s == f:
                cur = head
                while cur != s:
                    cur = cur.next
                    s = s.next
                return cur
        return