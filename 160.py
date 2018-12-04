# -*- coding: utf-8 -*-
# @创建时间 : 4/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        a, b = headA, headB
        la, lb = 0, 0
        while a:
            a = a.next
            la += 1
        while b:
            b = b.next
            lb += 1
        if a != b:
            return None
        a, b = headA, headB
        abdiff = abs(la - lb)
        if la > lb:
            while abdiff:
                a = a.next
                abdiff -= 1
        if la < lb:
            while abdiff:
                b = b.next
                abdiff -= 1
        while a != b:
            a = a.next
            b = b.next
        return a
