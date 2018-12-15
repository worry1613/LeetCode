# -*- coding: utf-8 -*-
# @创建时间 : 15/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)<3: return max(nums)
        # s = set(nums)
        # if len(s)<3: return max(list(s))
        # return sorted(list(s))[-3]

        listRes = sorted(list(set(nums)))
        if len(listRes) < 3:
            return listRes[len(listRes) - 1]
        else:
            return listRes[len(listRes) - 3]
