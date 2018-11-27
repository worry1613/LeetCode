# -*- coding: utf-8 -*-
# @创建时间 : 27/11/2018 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res=[]
        while queue:#当queue不为空时
            nodes=[]#存节点，每次循环前置空，每次只装一部分
            node_values=[]#存节点的值
            for node in queue:
                if node.left:
                    nodes.append(node.left)#将左子树装入队列中
                if node.right:
                    nodes.append(node.right)
                node_values+=[node.val]#因为每次循环node_values都会置空，所以最终结果保存在res里，node_values只是一小部分结果
            res.append(node_values)#实现从底到顶，node_values放前面.
            queue=nodes#将新添加的节点重新赋值给queue
        return res[::-1]

