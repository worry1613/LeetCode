# -*- coding: utf-8 -*-
# @创建时间 : 1/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        fast=1
        for slow in range(len(nums)-1):
            if nums[slow]!=nums[slow+1]:
                nums[fast]=nums[slow+1]
                fast+=1
        return fast