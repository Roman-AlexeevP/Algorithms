class Heap:

    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, a, depth):
        elements_count = pow(2, depth + 1) - 1
        self.HeapArray = [None] * elements_count
        if len(a) == 0:
            return None
        for number in a:
            self.Add(number)

    def get_max_child_index(self, i):
        left_child_index = (i * 2) + 1
        right_child_index = (i * 2) + 2
        if left_child_index > len(self.HeapArray) + 1 or right_child_index > len(self.HeapArray) + 1:
            return None
        if self.HeapArray[right_child_index] is None:
            return left_child_index
        if self.HeapArray[left_child_index] is None:
            return right_child_index

        if self.HeapArray[left_child_index] > self.HeapArray[right_child_index]:
            return left_child_index
        return right_child_index

    def GetMax(self):
        last_element_index = 0
        if self.HeapArray[last_element_index] is None:
            return -1
        while last_element_index < len(self.HeapArray) - 1 and self.HeapArray[last_element_index + 1] is not None:
            last_element_index += 1
        root = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[last_element_index]
        self.HeapArray[last_element_index] = None
        i = 0
        max_child_index = self.get_max_child_index(i)
        while i < len(self.HeapArray):
            if max_child_index is None:
                break
            if self.HeapArray[i] < self.HeapArray[max_child_index]:
                self.HeapArray[i], self.HeapArray[max_child_index] = self.HeapArray[max_child_index], \
                                                                     self.HeapArray[i]
            i = max_child_index
            max_child_index = self.get_max_child_index(i)
        return root

    def get_parent_index(self, i):
        return (i - 1) // 2

    def Add(self, key):
        if key is None:
            return None
        i = 0
        while self.HeapArray[i] is not None and i < len(self.HeapArray):
            i += 1
        if self.HeapArray[i] is not None:
            return False
        self.HeapArray[i] = key
        if i == 0:
            return True

        while i > 0 and self.HeapArray[i] > self.HeapArray[self.get_parent_index(i)]:
            self.HeapArray[i], self.HeapArray[self.get_parent_index(i)] = self.HeapArray[self.get_parent_index(i)], \
                                                                          self.HeapArray[i]
            i = self.get_parent_index(i)
        return True
