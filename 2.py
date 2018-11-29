# -*- coding: utf-8 -*-
# @创建时间 : 29/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 : return l2
        if not l2 : return l1
        add=0
        l = ListNode("X")
        r= l
        while (add or l1) and (add or l2):
            l1v= l1.val if l1 else 0
            l2v= l2.val if l2 else 0
            val =l1v+l2v+add
            val,add = val%10, val //10
            r.next=ListNode(val)
            # if val >9:
            #     r.next = ListNode(val-10)
            #     add=1
            # else:
            #     r.next=ListNode(val)
            #     add=0
            l1=l1.next if  l1 else None
            l2=l2.next if  l2 else None
            r=r.next
        if l1:
            r.next = l1
        if l2:
            r.next=l2
        return l.next