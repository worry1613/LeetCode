# -*- coding: utf-8 -*-
# @创建时间 : 15/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return list(set(range(1, len(nums)+1)) - set(nums))
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]