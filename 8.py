# -*- coding: utf-8 -*-
# @创建时间 : 29/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        _min = -2 ** 31
        _max = 2 ** 31 - 1
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        signs = ['-', '+']
        if not str:
            return 0
        elif len(str) == 1:
            if str[0] not in nums and str[0] not in signs:
                return 0
            elif str[0] in nums:
                return int(str[0])
            elif str[0] in signs:
                return 0
        if str[0] not in nums and str[0] not in signs:
            return 0
        flag = 1
        if str[0] == '-' and str[1] not in signs and str[1] in nums:
            flag = -1
            str = str[1:]
        if str[0] == '+':
            str = str[1:]
        for k, v in enumerate(str):
            if v not in nums:
                str = str[:k]
                break
        result = 0
        for k, v in enumerate(str[::-1]):
            result += int(v) * (10 ** k)
        if flag == -1:
            result = 0 - result
        if result > _max:
            return _max
        elif result < _min:
            return _min
        return result
