# -*- coding: utf-8 -*-
# @创建时间 : 11/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        快慢指针，h1基数指针，h2偶数指针
        """
        if not head or not head.next or not head.next.next: return head
        # if not head.next: return head
        # if not head.next.next : return head
        h1, h2, hh2 = head, head.next, head.next
        while h2 and h2.next:
            h1.next = h2.next
            h2.next = h2.next.next
            h1.next.next = hh2

            h1 = h1.next
            h2 = h2.next
        return head