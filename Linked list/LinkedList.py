class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def add_before_head(self, item):
        if self.head is None:
            self.tail = item
        else:
            item.next = self.head
        self.head = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        finded_nodes = []
        while node is not None:
            if node.value == val:
                finded_nodes.append(node)
            node = node.next
        return finded_nodes


    def delete(self, val, all=False):
        node = self.find(val)
        if node is None:
            return False
        if node is self.tail and node is self.head:
            self.head = self.tail = None
        elif node is self.head:
            self.head = self.head.next
        else:
            temp_node = self.head
            while temp_node.next is not node:
                temp_node = temp_node.next
            if node is self.tail:
                self.tail = temp_node
            temp_node.next = node.next
        if all:
            self.delete(val=val, all=all)
        return True

    def clean(self):
        node = self.head
        while node is not None:
            temp = node.next
            node = None
            node = temp
        self.tail = self.head = None

    def len(self):
        node = self.head
        list_len = 0
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_before_head(newNode)
        elif afterNode is self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode

