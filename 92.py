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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # count = 1
        # root = ListNode(0)
        # root.next = head
        # pre = root
        # while pre.next and count < m:
        #     pre = pre.next
        #     count += 1
        # if count < m:
        #     return head
        # mNode = pre.next
        # curr = mNode.next
        # while curr and count < n:
        #     next = curr.next
        #     curr.next = pre.next
        #     pre.next = curr
        #     mNode.next = next
        #     curr = next
        #     count += 1
        # return root.next

        if m == n or head.next is None: return head
        dummy = ListNode(None)
        dummy.next = head
        b1 = dummy
        for _ in range(m - 1):
            b1 = b1.next
        p = b1.next
        nh = p
        tmp = p.next
        for _ in range(n - m):
            nt = tmp
            tmp = nt.next
            nt.next = p
            p = nt
        b1.next = nt
        nh.next = tmp
        return dummy.next