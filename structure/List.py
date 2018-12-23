"""
线性表：零个或多个数据元素的有限序列。
关键的点就是表中的元素之前存在顺序关系，从前一个元素，能知道它的后一个元素。
线性表的表示有两种方式，一种直接在内存中划分出一段的联系空间，用于存储线性表中的元素，
这个就是顺序表；另一种就是链表。它们的区别先不管，首先来看看顺序表的实现。
Python 中有一个自带的数据类型，就是list，它就是顺序表的一种实现。
"""


class List(object):
    """定义顺序表类"""

    def __init__(self, max):
        """初始化，定义表的最大值"""
        self._elems = []
        self._length = 0
        self._max = max

    def len(self):
        """输入表的大小"""
        return self._length

    def push(self, value):
        """尾部添加元素"""
        if self._length == self._max:
            raise TypeError("push value faild: list already fill")
        self._elems.append(value)

    def pop(self):
        """尾部删除元素"""
        if _length == 0:
            raise TypeError("pop faild: list is empty")
        self._elems.pop()

    def index(self, value):
        """查看元素在表中的位置"""
        n = 0
        for i in self._elems:
            if i == value:
                return n
            n += 1
        raise ValueError("{} is not in list".format(value))

    def insert(self, key, value):
        """指定位置插入元素"""
        if self._length == self._max:
            raise TypeError("index value faild: list already fill")
        if key < 0 or key > self._length-1:
            raise TypeError("insert faild: range out of list")
        self._elems = self._elems[0:key] + value + self._elems[key+1:-1]

    def clear(self):
        """清空表"""
        self._elems = []
        self._length = 0

    def __repr__(self):
        return str(self._elems)

    def __str__(self):
        return self.__repr__()
