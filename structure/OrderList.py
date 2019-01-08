"""
线性表：零个或多个数据元素的有限序列。
关键的点就是表中的元素之前存在顺序关系，从前一个元素，能知道它的后一个元素。
线性表的表示有两种方式，一种直接在内存中划分出一段的联系空间，用于存储线性表中的元素，
这个就是顺序表；另一种就是链表。它们的区别先不管，首先来看看顺序表的实现。
Python 中有一个自带的数据类型，就是list，它就是顺序表的一种实现。
"""


class OrderList(object):
    """定义顺序表类"""

    def __init__(self):
        """初始化"""
        self._elems = []
        self._length = 0

    def prepend(self, value):
        """头部添加元素"""
        self._length += 1
        self._elems = [value] + self._elems

    def shift(self):
        """头部删除元素"""
        self._length -= 1
        self._elems = self._elems[1:]

    def append(self, value):
        """尾部添加元素"""
        self._length += 1
        self._elems.append(value)

    def pop(self):
        """尾部删除元素"""
        if self._length == 0:
            raise ValueError("list is empty")
        self._length -= 1
        self._elems.pop()

    def index(self, value):
        """查看元素在表中的位置"""
        n = 0
        for i in self._elems:
            if i == value:
                return n
            n += 1
        raise ValueError("{} is not in list".format(value))

    def insert(self, index, value):
        """指定位置插入元素"""
        if index < 0 or index > self._length-1:
            raise IndexError("range out of list")
        self._elems = self._elems[0:index] + [value] + self._elems[index:]

    def remove(self, index):
        """删除指定位置元素"""
        if index < 0 or index > self._length - 1:
            raise IndexError("range out of list")
        e = self._elems[index]
        self._elems = self._elems[0:index] + self._elems[index+1:]
        return e

    def clear(self):
        """清空表"""
        self._elems = []
        self._length = 0


    def reverse(self):
        """顺序表反转"""
        self._elems.reverse()

    def sort(self):
        self._elems.sort()

    def __len__(self):
        return self._length

    def __repr__(self):
        return str(self._elems)

    def __str__(self):
        return self.__repr__()
