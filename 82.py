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
        if not head.next: return head
        if head.val == head.next.val and not head.next.next: return []
        l = ListNode('X')
        l.next = head
        cur = l
        s, f = head, head.next
        while f:
            if s.val == f.val:
                f = f.next
            else:
                if s.next != f:
                    cur.next = f
                    s = f
                    f = f.next
                else:
                    s = s.next
                    f = f.next
                    cur = cur.next
        if s.next != f:
            cur.next = f

        return l.next


