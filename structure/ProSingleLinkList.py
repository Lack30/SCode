"""单链表变形
这里简单的变形，在内部添加一个指向尾部的节点，解决单链表尾部插入时
麻烦的问题
"""
from .singlelist import SingleList

class ProSingleLinkList(SingleList):
    def __init__(self):
        super(SingleList, self).__init__()
        self.rear = None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, self.head)
            self.rear = self.head
        else:
            self.head = Node(value, self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value, self.head)
            self.rear = self.head
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

    def pop(self):
        if self.head is None:
            raise IndexError("in pop_last")
        p = self.head
        if p.next is None:
            e = p.elem
            self.head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self.rear = p
        return e