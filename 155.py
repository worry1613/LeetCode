# -*- coding: utf-8 -*-
# @创建时间 : 4/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            if x <= self.stack[-1][1]:
                self.stack.append((x, x))
            else:
                self.stack.append((x, self.stack[-1][1]))

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()