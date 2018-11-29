# -*- coding: utf-8 -*-
# @创建时间 : 29/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if not s:
            return 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        s = s.upper()
        for k in range(l - 1):
            if d[s[k]] < d[s[k + 1]]:
                result -= d[s[k]]
            else:
                result += d[s[k]]
        return result + d[s[-1]]
