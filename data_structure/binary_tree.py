# -*- coding:utf-8 -*-
# 二叉树的实现

class Node(object):
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    # 层次遍历：使用队列
    def __repr__(self):
        if self.is_empty():
            return "The BinaryTree is empty!"
        queue = [self.root, ]
        result = []
        while queue:
            point = queue.pop(0)
            result.append(point.data)
            if point.lchild:
                queue.append(point.lchild)
            if point.rchild:
                queue.append(point.rchild)
        return str(result)

    # 层次遍历：使用队列
    def level_print(self):
        return str(self)

    # 先序遍历（递归实现“根左右”）
    def pre_print(self, start=None, result=[]):
        if self.is_empty():
            return "The BinaryTree is empty!"
        if start is None:
            start = self.root
        result.append(start.data)
        if start.lchild:
            self.pre_print(start.lchild, result)
        if start.rchild:
            self.pre_print(start.rchild, result)
        return result

    # 先序遍历（循环实现“根左右”）:使用栈
    def pre_print_loop(self):
        if self.is_empty():
            return "The BinaryTree is empty!"
        stack = [self.root, ]
        result = []
        while stack:
            point = stack.pop()
            result.append(point.data)
            if point.rchild:
                stack.append(point.rchild)
            if point.lchild:
                stack.append(point.lchild)
        return result

    # 中序遍历（递归实现“左根右”）
    def in_order(self, start=None, result=[]):
        if self.is_empty():
            return "The BinaryTree is empty!"
        if start is None:
            start = self.root
        if start.lchild:
            self.in_order(start.lchild, result)
        result.append(start.data)
        if start.rchild:
            self.in_order(start.rchild, result)
        return result

    # 中序遍历（循环实现“左根右”）
    def in_order_loop(self):
        if self.is_empty():
            return "The BinaryTree is empty!"
        stack = []
        result = []
        point = self.root
        while point or stack:
            while point:
                stack.append(point)
                point = point.lchild
            if stack:
                point = stack.pop()
                result.append(point.data)
                point = point.rchild
        return result

    # 后序遍历（递归实现“左右根”）
    def post_order(self, start=None, result=[]):
        if self.is_empty():
            return "The BinaryTree is empty!"
        if start is None:
            start = self.root
        if start.lchild:
            self.post_order(start.lchild, result)
        if start.rchild:
            self.post_order(start.rchild, result)
        result.append(start.data)
        return result

    # 后序遍历（循环实现“左右根”）
    def post_order_loop(self):
        if self.is_empty():
            return "The BinaryTree is empty!"
        # 循环实现“根右左”
        stack = [self.root, ]
        result = []
        while stack:
            point = stack.pop()
            result.append(point.data)
            if point.lchild:
                stack.append(point.lchild)
            if point.rchild:
                stack.append(point.rchild)
        # 翻转
        return result[::-1]

    # 树的镜像（递归实现）
    def reversed(self, start=None):
        if self.is_empty():
            return "The BinaryTree is empty!"
        if start is None:
            start = self.root

        temp = start.lchild
        start.lchild = start.rchild
        start.rchild = temp

        if start.lchild:
            self.reversed(start.lchild)
        if start.rchild:
            self.reversed(start.rchild)

    # 树的镜像（循环实现）：使用栈
    def reversed_loop(self):
        if self.is_empty():
            return "The BinaryTree is empty!"
        stack = [self.root, ]
        while stack:
            point = stack.pop()
            if point.lchild:
                stack.append(point.lchild)
            if point.rchild:
                stack.append(point.rchild)

            temp = point.lchild
            point.lchild = point.rchild
            point.rchild = temp

    # 树的深度（递归实现）
    def depth(self, start):
        if start is None:
            return 0
        leftDepth = self.depth(start.lchild)
        rightDepth = self.depth(start.rchild)
        return max(leftDepth + 1, rightDepth + 1)

    # 判断是否平衡二叉树
    def balance(self, start):
        if not start:
            return True
        if abs(self.depth(start.lchild) - self.depth(start.rchild)) > 1:
            return False
        else:
            return self.balance(start.lchild) and self.balance(start.rchild)

    # 树的重构
    """
    输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输    入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回二叉树的根节点。
    """

    def construct_tree(self, pre_order=[], mid_order=[]):
        if not pre_order or not mid_order:
            return None
        # 前序遍历的第一个结点一定是根结点
        root_data = pre_order[0]
        i = mid_order.index(root_data)
        # 递归构造左子树和右子树
        lchild = self.construct_tree(pre_order[1: 1 + i], mid_order[:i])
        rchild = self.construct_tree(pre_order[1 + i:], mid_order[i + 1:])
        return Node(root_data, lchild, rchild)

    # 搜索路径
    """
    输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。路径是从树的根节点开始往下一直到叶节点所经过的    节点形成一条路径。输出值为二维列表。
    """

    def route(self, start=None, total=0):
        result = []
        if not start:
            return result
        #  如果只有根节点或者找到叶子节点，我们就把其值返回
        if not start.lchild and not start.rchild and start.data == total:
            return [[start.data]]
        else:
            #  如果不是叶子节点，我们分别对根节点的左子树、右子树进行递归，注意修改变量:
            left = self.route(start.lchild, total - start.data)
            right = self.route(start.rchild, total - start.data)
            for item in left + right:
                result.append([start.data] + item)

        return result


"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class Solution(object):
    def HasSubtree(self, root1=None, root2=None):
        if not root1 or not root2:
            return False
        # 使用or相连，即其中只要有一个A的子树与B相同，则返回True
        return self.isEqual(root1, root2) or self.HasSubtree(root1.lchild, root2) or self.HasSubtree(root1.rchild,
                                                                                                     root2)

    # 以root1为根节点，判断A和B是否相等
    def isEqual(self, root1=None, root2=None):
        if not root2:
            return True
        if root1 and root2:
            if root1.data != root2.data:
                return False
            return self.isEqual(root1.lchild, root2.lchild) and self.isEqual(root1.rchild, root2.rchild)


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
k = Node("K")
a.lchild = b
b.rchild = c
c.lchild = d
a.rchild = e
e.rchild = f
f.lchild = g
g.lchild = h
g.rchild = k
binary_tree = BinaryTree()
binary_tree.root = a
print("二叉树结构：" + str(binary_tree))

print "二叉树层次遍历：" + binary_tree.level_print() + "\n"

print "二叉树先序遍历--递归实现：" + str(binary_tree.pre_print())
print "二叉树先序遍历--循环实现：" + str(binary_tree.pre_print_loop()) + "\n"

print "二叉树中序遍历--递归实现：" + str(binary_tree.in_order())
print "二叉树中序遍历--循环实现：" + str(binary_tree.in_order_loop()) + "\n"

print "二叉树后序遍历--递归实现：" + str(binary_tree.post_order())
print "二叉树后序遍历--循环实现：" + str(binary_tree.post_order_loop()) + "\n"

binary_tree.reversed()
print "二叉树的镜像--递归实现：" + str(binary_tree)
binary_tree.reversed_loop()
print "二叉树的镜像--循环实现：" + str(binary_tree) + "\n"

print "二叉树对的深度--递归实现：" + str(binary_tree.depth(a)) + '\n'

print "二叉树的重构：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。\n" \
      "假设输入的前序遍历和中序遍历的结果中都不含重复的数字。\n" \
      "例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，\n" \
      "则重建二叉树并返回二叉树的根节点。"
binary_tree2 = BinaryTree()
binary_tree2.root = binary_tree2.construct_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
print "重构后的二叉树：" + str(binary_tree2) + "\n"

print "输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。\n" \
      "路径是从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。"
result = binary_tree2.route(binary_tree2.root, 18)
print "目标整数为18，所有可能路径为：" + str(result) + '\n'

print "输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）"
tree_a = BinaryTree()
a = Node(8)
b = Node(8)
c = Node(7)
d = Node(9)
e = Node(2)
f = Node(4)
g = Node(7)
a.lchild = b
a.rchild = c
b.lchild = d
b.rchild = e
e.lchild = f
e.rchild = g
tree_a.root = a

tree_b = BinaryTree()
a = Node(8)
b = Node(9)
c = Node(2)
a.lchild = b
a.rchild = c
tree_b.root = a

print "A树：" + str(tree_a) + "\n" \
                            "B树：" + str(tree_b)

solution = Solution()
print "B树是否为A树的子树：" + str(solution.HasSubtree(tree_a.root, tree_b.root)) + "\n"

print "判断是否平衡二叉树："
print str(tree_a) + str(tree_a.balance(tree_a.root))
print str(tree_b) + str(tree_b.balance(tree_b.root))
print str(binary_tree) + str(binary_tree.balance(binary_tree.root))
print str(binary_tree2) + str(binary_tree2.balance(binary_tree2.root))
