# -*- coding: utf-8 -*-
# @创建时间 : 4/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) ==1 :return None
        d = dict()
        for k in range(len(numbers)):
            r = target - numbers[k]
            if r not in d:
                d[numbers[k]] = k
            else:
                return [d[r]+1,k+1]