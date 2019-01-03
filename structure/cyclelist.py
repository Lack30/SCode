"""循环单链表
在单链表的基础上将链表的最后一个节点指向头一个节点，使链表连成一个循环，
这样变形的好处就是将头尾插入花费效率相近了
"""
from .singlelist import Node

class CycleList:
    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear is None

    def lpush(self, value):
        """前端插入"""
        p = Node(value)
        if self.rear is None: 
            p.next = p # 建立一个节点的环
            self.rear = p
        else:
            p.next = self.rear.next
            self.rear.next = p

    def push(self, value):
        """尾端插入"""
        self.lpush(value)
        self.rear = self.rear.next

    def pop(self):
        """后端弹出"""
        if self.rear is None:
            raise IndexError("in pop of CycleList")
        p = self.rear.next
        if self.rear is p: # 链表只有一个节点的情况
            self.rear = None
        else:
            while p.next is not self.rear:
                p = p.next
            p.next = self.rear.next
            self.rear = p
        return p.elem

    def lpop(self):
        """前端弹出"""
        if self.rear is None:
            raise IndexError("in lpop of CycleList")
        p = self.rear.next
        if self.rear is p:
            self.rear = None
        else:
            self.rear.next = p.next
        return p.elem
