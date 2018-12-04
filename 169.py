# -*- coding: utf-8 -*-
# @创建时间 : 4/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rs = set(nums)
        # zs = len(nums)/2
        # for n in rs:
        #     if nums.count(n)>=zs:
        #         return n
        nums.sort()
        return nums[int(len(nums)/2)]