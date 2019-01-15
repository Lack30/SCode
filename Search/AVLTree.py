"""平衡二叉树
平衡二叉树是一类特殊的二叉排序树，它或为空，或者其左右子树
都是平衡二叉树，而且其左右子树高度之差绝对不超过1。

将二叉树上结点的左子树深度减去右子树深度的值称为平衡因子 BF (Balance Factor)，
所有结点上的BF只能为0,-1,1，只要有一个结点上BF的绝对值大于1，该二叉树就不平衡。
    BF为1：该结点的左子树结点数大于右子树节点数。
    BF为0：左右子树的节点数相同。
    BF为-1：该结点的左子树节点数小于右子树节点数。

在平衡二叉树失衡之后，重新恢复有四种情况：
    LL型（a的左子树较高，新节点插入在a的左子树的左子树）
    LR型（a的左子树较高，新结点插入在a的左子树的右子树）
    RR型（a的右子树较高，新结点插入在a的右子树的右子树）
    RL型（a的右子树较高，新节点插入在a的右子树的左子树）
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.bf = 0
        self.left = left
        self.right = right


class AVLBinTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def LL(a, b):
        a.left = b.right
        a.right = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def RR(a, b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        c = b.right
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:  # c本身就是插入结点
            a.bf = b.bf = 0
        elif c.bf == 1:  # 新节点在c的左子树
            a.bf = -1
            b.bf = 0
        else:  # 新节点在c的右子树
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        c = b.left
        a.right, c.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:  # c本身就是插入结点
            a.bf = 0
            b.bf = 0
        elif c.bf == 1:  # 新节点在c的左子树
            a.bf = 0
            b.bf = -1
        else:  # 新节点在c的右子树
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c

    def insert(self, data):
        a = p = self.root
        if a is None:
            self.root = Node(data)
            return
        pa = q = None  # 维持pa，q为a，p的父节点
        while p is not None:  # 确定插入位置及最小非平衡子树
            if data == p.data:  # data存在，直接赋值
                p.data = data
            if p.bf != 0:
                pa, a = q, p
            q = p
            if data < p.data:
                p = p.left
            else:
                p = p.right
        # q是插入点的父节点，pa，a记录最小非平衡子树
        node = Node(data)
        if data < q.data:
            q.left = node  # 作为左子树点
        else:
            q.right = node  # 或右子树点
        # 新结点已插入，a是最小不平衡子树
        if data < a.data:  # 新节点在a的左子树
            p = b = a.left
            d = 1
        else:  # 新结点在a的右子树
            p = b = a.right
            d = -1  # d记录新节点在a的那棵子树
        # 修改b到新结点路径上各节点的BF值，b为a的子节点
        while p != node:  # node一定存在，不用判断p空
            if data < p.data:
                p.bf = 1
                p = p.left
            else:  # p的右子树增高
                p.bf = -1
                p = p.right
        if a.bf == 0:  # a的原bf为0，不会失衡
            a.bf = d
            return
        if a.bf == -d:  # 新节点在较低的子树里
            a.bf = 0
            return
        # 新结点在较高子树，失衡，必须调整
        if d == 1:  # 新结点在a的左子树里
            if b.bf == 1:
                b = AVLBinTree.LL(a, b)  # LL调整
            else:
                b = AVLBinTree.LR(a, b)  # LR调整
        else:
            if b.bf == -1:
                b = AVLBinTree.RR(a, b)  # RR调整
            else:
                b = AVLBinTree.RL(a, b)  # RL调整
        if pa is None:  # 原a为树根，修改root
            self.root = b
        else:  # a非树根，新树接在正确位置
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b

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
    tree = AVLBinTree()
    for i in range(len(lis)):
        tree.insert(lis[i])
    print("先序排序：", tree.pre_order())
    print("中序排序：", tree.mid_order())
    print("后序排序：", tree.post_order())
