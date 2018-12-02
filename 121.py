# -*- coding: utf-8 -*-
# @创建时间 : 3/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        r = 0
        if not prices: return 0
        _min = prices[0]
        profit = 0
        for k,v in enumerate(prices):
            _min = min(_min,v)
            profit = max(v-_min,profit)
        return profit