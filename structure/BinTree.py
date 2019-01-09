"""二叉树
一种最简单的树形结构，其特点是树中每个结点至多关联到两个后继结点。

二叉树的性质
性质 1 :在二叉树的第 i 层上至多有 2e(i- 1) 个结点 (i >= 1 ) 。
性质 2: 深度为 k 的二叉树至多有 2e(k-1) 个结点 (k >= l) 。
性质 3: 对任何一棵二叉树 T，如果其叶子结点数为n0，度为 2 的结点数为n2，则 n0=n2+ 1 。
性质 4: 具有 n 个结点的完全二叉树的深度为 [log2n]+1 ( [x]表示不大于x的最大整数)。
性质 5: 如果对一棵有 n 个结点的完全二叉树(其深度为 [log2n]+1 ) 的结点按层序编
号(从第 1 层到第 [log2n]+1 层，每层从左到右) ，对任一结点 i (1<=i<= n)有:
    1.如果 i=1 ，则结点 i 是二叉树的根，无双亲;如果i> 1 ，则其双亲是结点
       [i/2] 。
    2.如果 2i>n ，则结点 i 无左孩子(结点 i 为叶子结点) ;否则其左孩子是结点
       2i 。
    3.如果 2i+1>n ，则结点 i 无右孩子;否则其右孩子是结点 2i+1 。
"""

"""完全二叉树
对一棵具有 n 个结点的二叉树按层序编号，如果编号为 i (l<=i<=n) 的结点与同
样深度的满二叉树中编号为 i 的结点在二叉树中位置完全相同，则这棵二叉树称为完
全二叉树。

特点：
1.叶子节点只能出现在最下层。
2.最下层的叶子一定集中在左部连续位置。
3.倒数二层，若有叶子结点，一定都在右部连续位置。
4.如果结点度为1，则该结点只有左孩子，即不存在只有右孩子树的情况。
5.同样节点树的二叉树，完全二叉树的深度最小。
"""


class BinTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinTree:
    def __init__(self):
        self.root = None

    def append(self, data):
        node = BinTNode(data)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.data]
        while len(q) == 0:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.data)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.data)
        return res

    def preorder(self, root):  # 先序遍历
        if root is None:
            return []
        result = [root.data]
        left = self.preorder(root.left)
        right = self.preorder(root.right)
        return result + left + right

    def inorder(self, root):  # 中序遍历
        if root is None:
            return []
        result = [root.data]
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        return left + result + right

    def postorder(self, root):  # 后序遍历
        if root is None:
            return []
        result = [root.data]
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        return left + right + result
