class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def add_in_tail(self, node):
        if self.head is None:
            self.head = node
            node.prev = None
            node.next = None
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def add_in_head(self, node):
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        node.next = self.head
        self.head = node
        node.prev = None

    def compare(self, v1, v2):
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
        return 0


    def add(self, value):
        node = Node(value)
        current_node = self.head
        if current_node is None:
            return self.add_in_tail(node)

        ordering = 1 if self.__ascending else -1
        while self.compare(value, current_node.value) == ordering:
            if current_node is self.tail:
                return self.add_in_tail(node)
            current_node = current_node.next
        if current_node is self.head:
            return self.add_in_head(node)

        node.next = current_node
        node.prev = current_node.prev
        current_node.prev.next = node
        current_node.prev = node

    def find(self, val):
        node = self.head
        ordering = 1 if self.__ascending else -1

        while node is not None:
            if self.compare(node.value, val) == ordering:
                return None
            if self.compare(node.value, val) == 0:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.find(val)
        if node is None:
            return False
        if node is self.head and node is self.tail:
            return self.clean(asc=self.__ascending)
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

    def clean(self, asc):
        self.__ascending = asc
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

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        return super(OrderedStringList, self).compare(v1.strip(), v2.strip())


