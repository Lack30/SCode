"""栈
栈也称为堆栈。
栈是一种容器，可存入数据元素、访问元素、删除元素。
栈的元素是后进后出关系的结构，简称为LIFO结构。
"""

class Node:
    """使用链表的方式表示栈"""
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class Stack:
    def __init__(self):
        self.top = None

    def push(self, elem):
        """入栈操作"""
        self.top = Node(elem, self.top)

    def pop(self):
        """出栈操作"""
        if self.top is None:
            raise ValueError("in Stack.pop()")
        p = self.top
        self.top = p.next
        return p.elem
