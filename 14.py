# -*- coding: utf-8 -*-
# @创建时间 : 29/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = len(strs)
        if not l:
            return ''
        elif l == 1:
            return strs[0]
        _min_str = min(strs, key=len)
        if not _min_str:
            return ''
        for k, v in enumerate(_min_str):
            for strnum in range(l):
                if strs[strnum][k] != v:
                    return _min_str[:k]
        return _min_str