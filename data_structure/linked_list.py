# -*- coding:utf8 -*-
# 实现单链表

class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.current = Node

    def __len__(self):
        return self.length

    def __iter__(self):
        self.current = self.head
        return self

    def next(self):
        if not self.current:
            raise StopIteration
        else:
            result = self.current.data
            self.current = self.current.next_node
            return result

    def __repr__(self):
        if self.is_empty():
            return "The LinkedList is null"
        else:
            result = []
            i = 0
            node = self.head
            while i < self.length:
                result.append(node.data)
                node = node.next_node
                i = i + 1
            return str(result)

    def is_empty(self):
        return self.length == 0

    def get_item(self, index):
        if self.is_empty():
            return "The LinkedList is null"

        if index < 0 or index >= self.length:
            return "The index is out of range"

        i = 0
        node = self.head
        while i < index and node.next_node:
            node = node.next_node
            i = i + 1

        if i == index:
            return node.data

    def get_index(self, data):
        if self.is_empty():
            return "The LinkedList is null"
        i = 0
        node = self.head
        while node:
            if node.data == data:
                return i
            else:
                node = node.next_node
                i = i + 1

        return "{} is not in the LinkedList".format(str(data))

    def append(self, data):
        self.length = self.length + 1
        item = Node(data)

        if not self.head:
            self.head = item
        else:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = item

    def insert(self, index, data):
        if self.is_empty():
            return "The LinkedList is null"
        if index < 0 or index >= self.length:
            return "The index is out of range"
        item = Node(data)
        self.length = self.length + 1

        if index == 0:
            node = self.head
            self.head = item
            item.next_node = node
        else:
            i = 0
            pre_node = self.head
            node = self.head
            while i < index:
                pre_node = node
                node = node.next_node
                i = i + 1
            pre_node.next_node = item
            item.next_node = node

    def delete(self, index):
        if self.is_empty():
            return "The LinkedList is empty"
        if index < 0 or index >= self.length:
            return "The LinkedList is out of range"
        self.length = self.length - 1

        if index == 0:
            self.head = self.head.next_node
        else:
            i = 0
            pre_node = self.head
            node = self.head
            while i < index:
                pre_node = node
                node = node.next_node
                i = i + 1
            pre_node.next_node = node.next_node

    def delete(self, data):
        if self.is_empty():
            return "The LinkedList is empty"
        node = self.head
        pre_node = None
        while node:
            if node.data == data:
                self.length = self.length - 1
                if not pre_node:
                    self.head = node.next_node
                else:
                    pre_node.next_node = node.next_node
            else:
                pre_node = node
            node = node.next_node

    def clear(self):
        self.head = None
        self.length = 0

    def update(self, index, data):
        if self.is_empty():
            return "The LinkedList is null"
        if index < 0 or index >= self.length:
            return "The index is out of range"

        i = 0
        node = self.head
        while i < index and node.next_node:
            node = node.next_node
            i = i + 1

        if i == index:
            node.data = data

    # 翻转链表
    def reversed(self):
        if not self.head:
            return "The LinkedList is null"
        current = self.head
        pre_node = None
        while current:
            next_one = current.next_node
            current.next_node = pre_node

            pre_node = current
            current = next_one
        self.head = pre_node

    # 判断是否存在环
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next_node
            while slow != fast:
                slow = slow.next_node
                fast = fast.next_node.next_node
            return True
        except:
            return False


linkedlist = LinkedList()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
e.next_node = a
linkedlist.head = a
print linkedlist
print(linkedlist.hasCycle(linkedlist.head))
