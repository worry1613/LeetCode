# -*- coding: utf-8 -*-
# @创建时间 : 2/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ps = path.split('/')
        stack = []
        for s in ps:
            if s == '' or s == '.' or (s == '..' and not stack):
                pass
            elif s == '..':
                stack.pop()
            else:
                stack.append(s)
        return '/' + '/'.join(stack)
