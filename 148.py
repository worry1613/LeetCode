# -*- coding: utf-8 -*-
# @创建时间 : 4/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        *************归并排序*********
        """
        if not head or not head.next: return head
        return self.mergesort(head)

    def mergesort(self, h):
        if not h.next:
            return h
        # 链表一分为二
        s, f = h, h
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        r = s.next
        s.next = None
        left = self.mergesort(h)
        right = self.mergesort(r)
        return self.merge(left, right)

    def merge(self, l, r):
        i, j = 0, 0
        result = ListNode('X')
        cur = result
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        if l:
            cur.next = l
        if r:
            cur.next = r
        return result.next
