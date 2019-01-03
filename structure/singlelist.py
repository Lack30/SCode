"""
单链表：是线性表的另一种实现方式。
由于顺序表是在内存中开辟一段连续的存储空间，如果出现反复修改结构的情况，
使用顺序表就不太方便，而且程序中如果需要巨大的线性表，用的顺序表实现也
会操作内存关系上的困难。
单链表就能很好的解决这些问题，由于单链表的各个节点是通过一个指针来指向
它的下一个节点，所以在内存中存储位置是随机的。但它需要在每个节点中额外
添加一个位置指向下一个节点的位置，所以需要话费的总空间大于顺序表。
"""


class Node:
    """单链表的节点
    """

    def __init__(self, elem, next=None):
        """初始化一个新节点
        :elem object 节点的元素值
        :next object 下一个节点的位置
        """
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __repr__(self):
        return self.__str__()


class SingleList():
    def __init__(self):
        self._length = 0
        self.head = None


    def is_empty(self):
        return self._length == 0 and self.head is None

    def lpush(self, value):
        """头部添加元素"""
        self._length += 1
        self.head = Node(value, self.head)

    def lpop(self):
        """删除头部"""
        if self.head is None:
            raise IndexError("single list is empty")
        self._length -= 1
        e = self.head.elem
        self.head = self.head.next
        return e

    def push(self, value):
        """尾部添加元素"""
        self._length += 1
        # 第一种情况，如果链表为空，直接添加头部
        if self.head is None:
            self.head = Node(value)
            return
        # 第二种情况，需要循环取得尾部元素，再添加
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)

    def pop(self):
        """尾部删除元素"""
        # 空表报错
        if self.head is None:
            raise IndexError("single list is empty")
        self._length -= 1
        p = self.head
        # 链表中只有一个元素
        if p.next is None:
            e = p.elem
            self.head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.elem
        p.next = None
        return e

    def index(self, value):
        """输出元素在表中的位置"""
        if self.head is None:
            raise ValueError("{} is not in single list".format(value))
        n = 0
        if self.head.elem == value:
            return n
        p = self.head
        while p.next is not None:
            n += 1
            p = p.next
            if p.elem == value:
                return n
        raise ValueError("{} is not in single list".format(value))

    def insert(self, index, value):
        """在指定位置插入元素"""
        if index < 0 or index > self._length-1:
            raise IndexError("single list out of range")
        self._length += 1
        if index == 0 and self.head is None:
            self.head = Node(value)
            return
        p = self.head
        for i in range(index):
            p = p.next
        p.next = Node(value, p.next)

    def remove(self, index):
        """删除指定位置的元素"""
        if index < 0 or index > self._length-1:
            raise IndexError("single list out of range")
        if self.head is None:
            raise IndexError("single list is empty")
        self._length -= 1
        p = self.head
        for i in range(index-1):
            p = p.next
        e = p.next.elem
        p.next = p.next.next
        return e

    def reverse(self):
        """链表反转"""
        if self.head is None:
            return
        dummp = Node(-1, self.head)
        prev = dummp.next
        pcur = prev.next
        while pcur is not None:
            prev.next = pcur.next
            pcur.next = dummp.next
            dummp.next = pcur
            pcur = prev.next
        self.head = dummp.next

    def __len__(self):
        return self._length

    def __repr__(self):
        l = []
        p = self.head
        while p.next is not None:
            l.append(p.elem)
            p = p.next
        l.append(p.elem)
        return str(l)

    def __str__(self):
        return self.__repr__()


"""单链表变形
这里简单的变形，在内部添加一个指向尾部的节点，解决单链表尾部插入时
麻烦的问题
"""
class ProSingleList(SingleList):
    def __init__(self):
        super(SingleList, self).__init__()
        self.rear = None

    def lpush(self, value):
        if self.head is None:
            self.head = Node(value, self.head)
            self.rear = self.head
        else:
            self.head = Node(value, self.head)

    def push(self, value):
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


