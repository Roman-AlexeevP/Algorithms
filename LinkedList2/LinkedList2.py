class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
        node = self.head
        while node is not None:
            if node.value == val:
                if node is self.head and node is self.tail:
                    self.tail = self.head = None
                    return True
                elif node is self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif node is self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                if not all:
                    break
            node = node.next

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
            if self.head is None:
                self.add_in_head(newNode)
            else:
                self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next.prev = newNode
            afterNode.next = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        newNode.prev = None

