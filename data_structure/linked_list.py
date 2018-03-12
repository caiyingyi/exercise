# -*- coding:utf-8 -*-
# 实现单链表

class Node(object):
    def __init__(self, data, next_one=None):
        self.data = data
        self.next_one = next_one


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.current = None

    def is_empty(self):
        return self.head is None

    # 可迭代对象
    def __iter__(self):
        self.current = self.head
        return self

    # 迭代器
    def next(self):
        if not self.current:
            raise StopIteration
        else:
            result = self.current.data
            self.current = self.current.next_one
            return result

    def __repr__(self):
        if self.is_empty():
            return "The LinkedList is empty!"
        else:
            point = self.head
            result = []
            while point:
                result.append(point.data)
                point = point.next_one
            return str(result)

    def append(self, data):
        node = Node(data)
        self.length = self.length + 1
        if self.is_empty():
            self.head = node
        else:
            point = self.head
            while point.next_one:
                point = point.next_one
            point.next_one = node

    def insert(self, data, index):
        if index < 0 or index >= self.length:
            print("The index in out of range!")
        else:
            node = Node(data)
            self.length = self.length + 1

            if index == 0:
                node.next_one = self.head
                self.head = node
            else:
                pre_node = self.head
                i = 0
                while i < index - 1:
                    pre_node = pre_node.next_one
                    i = i + 1
                node.next_one = pre_node.next_one
                pre_node.next_one = node

    def get_item(self, index):
        if index < 0 or index >= self.length:
            print "The index is out of range!"
        else:
            i = 0
            point = self.head
            while i < index:
                point = point.next_one
                i = i + 1
            return point.data

    def get_index(self, data):
        if self.is_empty():
            print "The LinkedList is empty!"
        else:
            i = 0
            point = self.head
            while i < self.length:
                if point.data == data:
                    return i
                else:
                    point = point.next_one
                    i = i + 1
            print "the {} is not in the LinkedList".format(data)

    def update(self, index, data):
        if index < 0 or index >= self.length:
            print "The index is out of range!"
        else:
            i = 0
            point = self.head
            while i < index:
                i = i + 1
                point = point.next_one
            point.data = data

    def delete(self, index):
        if index < 0 or index >= self.length:
            print "The index is out of range!"
        else:
            self.length = self.length - 1

            if index == 0:
                self.head = self.head.next_one
            else:
                pre_node = self.head
                i = 0
                while i < index - 1:
                    i = i + 1
                    pre_node = pre_node.next_one
                pre_node.next_one = pre_node.next_one.next_one

    def delete2(self, data):
        index = self.get_index(data)
        if index:
            self.delete(index)

    def clear(self):
        self.head = None
        self.length = 0

    # 翻转链表
    def reversed(self):
        if self.is_empty():
            return
        pre_node = None
        point = self.head
        while point:
            next_node = point.next_one
            point.next_one = pre_node
            pre_node = point
            point = next_node

        self.head = pre_node

    # 判断单链表是否环
    def hasCycle(self):
        try:
            slow = self.head
            fast = self.head.next_one
            while slow != fast:
                slow = slow.next_one
                fast = fast.next_one.next_one
            return True
        except:
            return False


linked_list = LinkedList()
for one in range(1, 11):
    linked_list.append(one)
print "原单链表：" + str(linked_list)

linked_list.insert("X", 2)
print "在原单链表索引为2处插入X：" + str(linked_list)

print "单链表中索引为2的结点值为：" + str(linked_list.get_item(2))

print "值为9的结点在单链表中的索引值为：" + str(linked_list.get_index(9))

linked_list.update(3, "Y")
print "把原单链表中索引为3的结点值修改为Y：" + str(linked_list)

linked_list.delete(10)
print "删除单链表中索引为10的结点值：" + str(linked_list)

linked_list.delete2("Y")
print "删除单链表中值为Y的结点：" + str(linked_list)

# linked_list.clear()
# print "清空单链表：" + str(linked_list)

linked_list.reversed()
print "翻转单链表：" + str(linked_list)

print "单链表是否存在环：" + str(linked_list.hasCycle())

print "实现迭代器：\n"
a = iter(linked_list)
print "迭代第一次：" + str(a.next())
print "迭代第二次：" + str(a.next())

