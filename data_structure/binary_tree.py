# -*- coding:utf8 -*-
class Node(object):
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.is_empty():
            return "The tree is empty."
        result = []
        queue = []
        queue.append(self.root)
        while queue:
            point = queue.pop(0)
            result.append(point.data)
            if point.lchild:
                queue.append(point.lchild)
            if point.rchild:
                queue.append(point.rchild)
        return str(result)

    def add(self, data):
        node = Node(data)

        if self.is_empty():
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                point = queue.pop(0)
                if not point.lchild:
                    point.lchild = node
                    return
                elif not point.rchild:
                    point.rchild = node
                    return
                else:
                    queue.append(point.lchild)
                    queue.append(point.rchild)

    # 层次遍历
    def level_print(self):
        return self.__repr__()

    # 前序遍历（循环实现）
    def pre_print_loop(self):
        if self.is_empty():
            return "The tree is empty"
        result = []
        stack = []
        point = self.root
        while point or stack:
            while point:
                stack.append(point)
                result.append(point.data)
                point = point.lchild
            if stack:
                point = stack.pop().rchild
        return result

    # 前序遍历（递归实现）
    def pre_print(self, start=None):
        if not start:
            start = self.root
        print start.data,
        if start.lchild:
            self.pre_print(start.lchild)
        if start.rchild:
            self.pre_print(start.rchild)

    # 中序遍历（循环实现）
    def in_order_loop(self):
        if self.is_empty():
            return "The tree is empty"
        result = []
        stack = []
        point = self.root
        while point or stack:
            while point:
                stack.append(point)
                point = point.lchild
            if stack:
                point = stack.pop()
                result.append(point.data)
                point = point.rchild
        return str(result)

    # 中序遍历（递归实现）
    def in_order(self, start=None):
        if not start:
            start = self.root
        if start.lchild:
            self.in_order(start.lchild)
        print start.data,
        if start.rchild:
            self.in_order(start.rchild)

    # 后序遍历（循环实现）
    def post_order_loop(self):
        if self.is_empty():
            return "The tree is empty"
        point = self.root
        result = []
        stack = []
        while point or stack:
            while point:
                result.append(point.data)
                stack.append(point)
                point = point.rchild
            if stack:
                point = stack.pop().lchild
        return result[::-1]

    # 后序遍历（递归实现）
    def post_order(self, start=None):
        if not start:
            start = self.root
        if start.lchild:
            self.post_order(start.lchild)
        if start.rchild:
            self.post_order(start.rchild)
        print start.data,

    def is_empty(self):
        return not self.root

    # 合并两棵树
    def mergeTrees(self, t1, t2, new=None):
        if not t1 and not t2:
            return
        ans = Node((t1.data if t1 else 0) + (t2.data if t2 else 0))
        if t1 == self.root:
            new.root = ans
        ans.lchild = self.mergeTrees(t1 and t1.lchild, t2 and t2.lchild)
        ans.rchild = self.mergeTrees(t1 and t1.rchild, t2 and t2.rchild)
        return ans

    def merge_trees(self, other):
        new = BinaryTree()
        self.mergeTrees(self.root, other.root, new)
        return new

    # 翻转树
    def reversed(self, start=None):
        if not start:
            start = self.root
        temp = start.lchild
        start.lchild = start.rchild
        start.rchild = temp
        if start.lchild:
            self.reversed(start.lchild)
        if start.rchild:
            self.reversed(start.rchild)

    # 判断树是否相同
    def isSameTree(self, p, q):
        if p and q:
            return p.data == q.data and self.isSameTree(p.lchild, q.lchild) and self.isSameTree(p.rchild, q.rchild)
        return p is q


tree = BinaryTree()
arr = range(8)
for one in arr:
    tree.add(one)
print "Tree:" + str(tree) + "\n"

tree_ = BinaryTree()
arr = range(10)
for one in arr:
    tree_.add(one)
print "Tree_:" + str(tree_) + "\n"

print(tree.isSameTree(tree.root, tree_.root))


# 合并树
# print(str(tree.merge_trees(tree_)))

# 翻转树
# tree.reversed()
# print(str(tree))

# 层次遍历
# print "level_print:" + str(tree.level_print()) + "\n"

# 前序遍历（循环实现）
# print "pre_print_loop:" + str(tree.pre_print_loop()) + "\n"

# 中序遍历（循环实现）
# print "in_order_loop:" + str(tree.in_order_loop()) + "\n"

# 中序遍历（循环实现）
# print "post_order_loop:" + str(tree.post_order_loop()) + "\n"

# 前序遍历（递归实现）
# print "pre_print:"
# tree.pre_print()

# 中序遍历（递归实现）
# print "\n" + "in_order:"
# tree.in_order()

# 后序遍历（递归实现）
# print "\n" + "post_order:"
# tree.post_order()
