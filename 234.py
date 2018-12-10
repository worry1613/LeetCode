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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        快慢指针+反转
        """
        if not head: return True
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        prev = None
        while cur:
            h = cur.next
            cur.next = prev
            prev = cur
            cur = h
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True