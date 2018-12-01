# -*- coding: utf-8 -*-
# @创建时间 : 1/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = ListNode('X')
        l.next = head
        if not head: return l.next
        if not head.next and n == 1: return
        c = 1
        s, f = l, l.next
        while c < n and f:
            f = f.next
            c += 1
        while f and f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return l.next


