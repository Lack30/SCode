"""队列
队列又称为队，也是一种容器，可存入元素，访问元素，删除元素，
队列的元素遵行先进先出的原则，即FIFO
"""

class Node:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class Queue:
    def __init__(self):
        self.rear = None

    def enqueue(self, elem):
        """入队操作"""
        p = Node(elem)
        if self.rear is None:
            self.rear = p
            self.rear.next = self.rear
        else:
            p.next = self.rear.next
            self.rear.next = p
            self.rear = p

        

    def denqueue(self):
        """出队操作"""
        if self.rear is None:
            raise ValueError("in denqueue in Queue")
        p = self.rear.next
        if p is self.rear:
            self.rear = None
            return p.elem
        self.rear.next = p.next
        return p.elem


    def printall(self):
        if self.rear is None:
            return
        p = self.rear.next
        while p is not self.rear:
            print(p.elem, end=" ")
            p = p.next
        print(p.elem)

