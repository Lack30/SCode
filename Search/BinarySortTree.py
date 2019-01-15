"""二叉排序树
二傻排序树是一种在结点里存储数据的二叉树。一棵二叉排序树或者为空，
或者具有以下性质：
    其根结点保存着一个数据项。
    如果其左子树不为空，那么其左子树的所有结点保存的值均小于它根节点保存的值。
    如果其右子树不为空，那么其右子树的所有结点保存的值均大于它根结点保存的值。
    非空的左子树或右子树也是二叉排序树。
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinSortTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def search(self, key):
        bt = self.root
        while bt is not None:
            entry = bt.data
            if key < entry:
                bt = bt.left
            elif key > entry:
                bt = bt.right
            else:
                return entry
        return None

    def insert(self, key):
        if self.is_empty():
            self.root = Node(key)
        bt = self.root
        while True:
            entry = bt.data
            if key < entry:
                if bt.left is None:
                    bt.left = Node(key)
                bt = bt.left
            elif key > entry:
                if bt.right is None:
                    bt.right = Node(key)
                bt = bt.right
            else:
                bt.data = key
                return

    def delete(self, key):
        p, q = None, self.root
        while q and q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            if q is None:
                return

        if q.left is None:
            if p is None:
                self.root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return

        r = q.left
        while r.right is None:
            r = r.right
        r.right = q.right
        if p is None:
            self.root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def _pre_order(self, node=None):
        if node is None:
            node = self.root
        yield node.data
        if node.left is not None:
            for item in self._pre_order(node.left):
                yield item
        if node.right is not None:
            for item in self._pre_order(node.right):
                yield item

    def _mid_order(self, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            for item in self._mid_order(node.left):
                yield item
        yield node.data
        if node.right is not None:
            for item in self._mid_order(node.right):
                yield item

    def _mid_order1(self):
        node, s = self.root, []
        while node or s:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            yield node.data
            node = node.right

    def _post_order(self, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            for item in self._post_order(node.left):
                yield item
        if node.right is not None:
            for item in self._post_order(node.right):
                yield item
        yield node.data

    def pre_order(self):
        return list(self._pre_order())

    def mid_order(self):
        return list(self._mid_order1())

    def post_order(self):
        return list(self._post_order())


if __name__ == '__main__':
    lis = [62, 58, 88, 47, 73, 99, 35, 51, 93, 37]
    bs_tree = BinSortTree()
    for i in range(len(lis)):
        bs_tree.insert(lis[i])
    bs_tree.delete(73)
    print("先序排序：", bs_tree.pre_order())
    print("中序排序：", bs_tree.mid_order())
    print("后序排序：", bs_tree.post_order())