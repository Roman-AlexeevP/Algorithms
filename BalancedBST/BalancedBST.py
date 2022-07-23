class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        if len(a) == 0:
            return []
        array = sorted(a)
        self.build_bst(array, None, 0, len(array) - 1)

    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        left_height = self.get_height(root_node.LeftChild)
        right_height = self.get_height(root_node.RightChild)
        difference = abs(left_height - right_height)

        is_balanced_left = self.IsBalanced(root_node.LeftChild)
        is_balanced_right = self.IsBalanced(root_node.RightChild)
        is_balanced = difference <= 1 and is_balanced_right and is_balanced_left
        return is_balanced

    def get_height(self, root):
        if root is None:
            return 0
        height_right = self.get_height(root.RightChild)
        height_left = self.get_height(root.LeftChild)
        height = height_left if height_left > height_right else height_right
        return height + 1

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

        node.LeftChild = self.build_bst(array, node, left, middle - 1)
        node.RightChild = self.build_bst(array, node, middle + 1, right)
        return node
