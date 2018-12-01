# -*- coding: utf-8 -*-
# @创建时间 : 1/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2 > 0: return False
        d = {')': '(', '}': '{', ']': '['}
        st = [0]
        for v in s:
            if v not in d:
                st.append(v)
            else:
                if d[v] != st.pop():
                    return False
        return False if len(st) > 1 else True

