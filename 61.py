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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        if k == 0: return head
        c = 1
        cur = head
        while cur.next:
            cur = cur.next
            c += 1
        tail = cur
        m = c - k % c
        l = ListNode('x')
        l.next = head
        cur = l
        c = 0
        while cur:
            if c == m:
                tail.next = head
                head = cur.next
                cur.next = None
                return head
            else:
                c += 1
                cur = cur.next

        return head