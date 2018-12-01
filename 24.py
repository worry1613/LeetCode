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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None or head.next is None: return head
        # dummy = ListNode(0)
        # dummy.next = head
        # p = dummy
        # while p.next and p.next.next:
        #     tmp = p.next.next
        #     p.next.next = tmp.next
        #     tmp.next = p.next
        #     p.next = tmp
        #     p = p.next.next
        # return dummy.next

        fake_head = ListNode(0)
        fake_head.next = head
        prev = fake_head

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return fake_head.next