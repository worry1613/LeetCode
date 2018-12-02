# -*- coding: utf-8 -*-
# @创建时间 : 3/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [0 for i in range(n + 1)]
        num[0] = 1
        num[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                num[i] += num[j - 1] * num[i - j]

        return num[n]