# -*- coding: utf-8 -*-
# @创建时间 : 11/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        stack = []
        si = [str(i) for i in range(10)]  # 0-9
        sc = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # a-z
        e = ''
        for c in s:
            if c == '[':
                e += '*('
            elif c == ']':
                e = e[:-1] + ')+'
            elif c in si:
                e += c
            else:
                e += '\'' + c + '\'+'
        if e[-1] == '+': e = e[:-1]
        return eval(e)
