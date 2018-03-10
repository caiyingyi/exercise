# -*- coding:utf8 -*-
class Node(object):
    def __init__(self, data, next_one=None, prev_one=None):
        self.data = data
        self.next_one = next_one
        self.prev_one = prev_one


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.current = None

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
            self.current = self.current.next_one
            return result

    def __repr__(self):
        return str(list(iter(self)))

    # 在链表末尾添加元素
    def push(self, data):
        self.length = self.length + 1
        if self.tail:
            node = Node(data, None, self.tail)
            self.tail.next_one = node
        else:
            node = Node(data)
            self.head = node
        self.tail = node

    # 删除链表末尾元素
    def pop(self):
        if self.length:
            self.length = self.length - 1
            result = self.tail.data
            self.tail = self.tail.prev_one
            if self.tail:
                self.tail.next_one = None
            else:
                self.head = None
            return result
        else:
            raise ValueError('The list is null')

    # 在链表首部删除元素
    def shift(self):
        if self.length:
            self.length = self.length - 1
            result = self.head.data
            self.head = self.head.next_one
            if self.head:
                self.head.prev_one = None
            else:
                self.tail = None
            return result
        else:
            raise ValueError('The list is null!')

    # 在链表首部添加元素
    def unshift(self, data):
        self.length = self.length + 1
        if self.head:
            temp = Node(data, self.head, None)
            self.head.prev_one = temp
        else:
            temp = Node(data)
            self.tail = temp
        self.head = temp

    def __getitem__(self, index):
        if not self.length:
            return "The list is null"
        if index < 0 or index >= self.length:
            return "The index is out of range"
        i = 0
        node = self.head
        while i < index:
            node = node.next_one
            i = i + 1
        return node

    def get_item(self, index):
        result = self.__getitem__(index)
        if type(result) == str:
            return result
        else:
            return result.data

    def get_index(self, data):
        if not self.length:
            return "The list is null"
        i = 0
        node = self.head
        while node:
            if node.data == data:
                return i
            else:
                i = i + 1
                node = node.next_one
        return "{} is not in the list".format(str(data))

    def insert(self, index, data):
        if not self.length:
            return "The list is null"
        if index < 0 or index >= self.length:
            return "The index is out of range"
        self.length = self.length + 1

        next_node = self.__getitem__(index)
        pre_node = next_node.prev_one
        target = Node(data, next_node, pre_node)
        pre_node.next_one = target
        next_node.prev_one = target

        if index == 0:
            self.head = target

    def update(self, index, data):
        if not self.length:
            return "The list is null"
        if index < 0 or index >= self.length:
            return "The index is out of range"

        node = self.__getitem__(index)
        node.data = data

    def delete(self, index):
        if not self.length:
            return "The list is null"
        if index < 0 or index >= self.length:
            return "The index is out of range"
        node = self.__getitem__(index)
        pre_node = node.prev_one
        next_node = node.next_one
        if not pre_node and not next_node:
            self.head = None
            self.tail = None
        elif not pre_node and next_node:
            self.head = next_node
            next_node.prev_one = None
        elif pre_node and not next_node:
            self.tail = pre_node
            pre_node.next_one = None
        else:
            pre_node.next_one = next_node
            next_node.prev_one = pre_node
        self.length = self.length - 1

    def reversed(self):
        if self.length == 0:
            return "The list is empty"
        if self.length == 1:
            return
        else:
            node = self.head
            head = self.tail
            self.tail = node
            while node:
                pre_node = node.prev_one
                next_node = node.next_one
                node.prev_one = next_node
                node.next_one = pre_node
                node = next_node
            self.head = head




linklist = LinkedList()
linklist.push(1)
linklist.push(2)
linklist.push(3)
linklist.push(4)
linklist.push(5)
linklist.unshift(0)

print linklist
linklist.reversed()
print linklist
