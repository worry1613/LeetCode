# -*- coding: utf-8 -*-
# @创建时间 : 10/12/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = []
        self.tp = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.st.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.st:
            self.tp.append(self.st.pop())
        r = self.tp.pop()
        while self.tp:
            self.st.append(self.tp.pop())
        return r

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.st:
            self.tp.append(self.st.pop())
        r = self.tp[-1]
        while self.tp:
            self.st.append(self.tp.pop())
        return r

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.st

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()