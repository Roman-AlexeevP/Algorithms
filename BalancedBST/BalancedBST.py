class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        if len(a) == 0:
            return []
        array = sorted(a)
        self.build_bst(array,None, 0, len(array) - 1)

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node

    def build_bst(self, array, root, left, right):
        if left > right:
            return None
        middle = left + ((right - left) // 2)
        key = array[middle]
        node = BSTNode(key=key, parent=root)

        if self.Root is None:
            self.Root = node

        node.Level = 0
        if root is not None:
            node.Level = root.Level + 1

        node.LeftChild = self.build_bst(array, node, left, middle-1)
        node.RightChild = self.build_bst(array, node, middle+1, right)
        return node

    def WideAllNodes(self):
        all_nodes = []
        if self.Root is None:
            return []
        all_nodes.append(self.Root.NodeKey)
        nodes_queue = [self.Root, ]
        while nodes_queue:
            node = nodes_queue.pop(0)
            if node.LeftChild is not None:
                all_nodes.append(node.LeftChild.NodeKey)
                nodes_queue.append(node.LeftChild)
            if node.RightChild is not None:
                all_nodes.append(node.RightChild.NodeKey)
                nodes_queue.append(node.RightChild)

        return tuple(all_nodes)