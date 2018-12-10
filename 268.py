# -*- coding: utf-8 -*-
# @创建时间 : 10/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return (int(len(nums)*(len(nums)+1)/2)-sum(nums))
        i = 0
        nums.sort()
        for item in nums:
            if item - i != 0:
                return i
            else:
                i += 1
        return i
