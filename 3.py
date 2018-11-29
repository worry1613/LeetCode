# -*- coding: utf-8 -*-
# @创建时间 : 29/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        _max = 2 ** 31 - 1
        _min = -2 ** 31
        if x > _max or x < _min:
            return 0
        result = 0
        flag = 0
        if x == 0:
            return 0
        elif x < 0:
            flag = -1
            x = 0 - x

        while x:
            result = result * 10 + x % 10
            if result > _max or result < _min:
                return 0
            x //= 10
        return result if flag > -1 else 0 - result
