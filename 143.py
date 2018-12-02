# -*- coding: utf-8 -*-
# @创建时间 : 3/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # if not head or not head.next or not head.next.next: return
        # s = []
        # cur = head
        # while cur:
        #     s.append(cur)
        #     cur = cur.next
        # r = len(s)-1
        # cur,nex = head,head.next
        # while nex.next != s[r] :
        #     cur.next = s[r]
        #     s[r].next = nex
        #     s[r-1].next = s[r].next
        #     cur = nex
        #     nex = nex.next
        #     r-=1
        # return head
        # # 以上代码超时了，可能是因为数组的原因吧
        if head and head.next and head.next.next:
            # 快慢指针，找到后半段结点
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head1 = head
            head2 = slow.next
            slow.next = None
            # 反转后半段结点
            dummy = ListNode(0)
            dummy.next = head2
            p = head2.next
            head2.next = None
            while p:
                temp = p
                p = p.next
                temp.next = dummy.next
                dummy.next = temp
            head2 = dummy.next
            # 合并链表
            p1 = head1
            p2 = head2
            while p2:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp1
                p1 = temp1
                p2 = temp2
