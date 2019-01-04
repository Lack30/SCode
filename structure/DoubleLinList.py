"""双链表
单链表只有一个方向的链接，只能做一个方向的扫描和逐步操作。
如果希望两端都能高效的完成插入/删除操作，就需要用到双链表。
"""

class DNode:
    """双链表的节点，包含元素，下一个节点的链接，上一个节点的链接"""
    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.prev = prev
        self.next = next_

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.rear = None

    def prepend(self, value):
        """前端插入"""
        p = DNode(value, self.rear, self.head)
        if self.head is None:
            self.rear = p
        else:
            p.next.prev = p
        self.head = p

    def append(self, value):
        """后端插入"""
        p = DNode(value, self.rear, None)
        if self.head is None: # 空表
            self.head = p
        else:
            p.prev.next = p
        self.rear = p

    def pop(self):
        """后端删除"""
        if self.head is None:
            raise IndexError("in pop of DoubleLinkList")
        e = self.rear.elem
        self.rear = self.rear.prev
        if self.rear is None:
            self.head = None
        else:
            self.rear.next = None
        return e

    def shift(self):
        """前端删除"""
        if self.head is None:
            raise IndexError("in shift of DoubleLinkList")
        e = self.head.elem
        self.head = self.head.next
        if self.head is None:
            self.rear = None
        else:
            self.head.prev = None
        return e