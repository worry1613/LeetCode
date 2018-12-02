# -*- coding: utf-8 -*-
# @创建时间 : 2/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return [1]
        i = 0
        l = len(digits)
        for dg in range(l):
            i += digits[dg] * 10 ** (l - 1 - dg)
        i += 1
        return [int(ii) for ii in str(i)]
