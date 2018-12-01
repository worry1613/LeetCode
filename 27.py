# -*- coding: utf-8 -*-
# @创建时间 : 1/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        fast=0
        for slow in range(len(nums)):
            if nums[slow] !=val:
                nums[fast] = nums[slow]
                fast+=1
        return fast