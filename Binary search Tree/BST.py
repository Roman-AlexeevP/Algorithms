class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None

    def is_leaf(self):
        return self.RightChild is None and self.LeftChild is None


class BSTFind:

    def __init__(self):
        self.Node = None

        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        find_result = BSTFind()
        if self.Root is None or key is None:
            return find_result
        find_result.Node = self.Root
        if self.Root.NodeKey == key:
            find_result.NodeHasKey = True
            return find_result
        if key < self.Root.NodeKey:
            if self.Root.LeftChild is None:
                find_result.ToLeft = True
                return find_result
            tree = BST(self.Root.LeftChild)
            return tree.FindNodeByKey(key)
        if key > self.Root.NodeKey:
            if self.Root.RightChild is None:
                return find_result
            tree = BST(self.Root.RightChild)
            return tree.FindNodeByKey(key)

        return find_result

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey:
            return False
        node = BSTNode(key=key, val=val, parent=None)
        if find_result.Node is None:
            self.Root = node
            return True
        node.Parent = find_result.Node
        if find_result.ToLeft:
            find_result.Node.LeftChild = node
            return True
        find_result.Node.RightChild = node
        return True

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return None
        node = FromNode.RightChild if FindMax else FromNode.LeftChild
        if node is None:
            return FromNode
        tree = BST(node)
        return tree.FinMinMax(node, FindMax)

    def DeleteNodeByKey(self, key):
        deleted_node = self.FindNodeByKey(key).Node
        if deleted_node is None:
            return False
        if deleted_node.is_leaf():
            return self.remove_node_from_parent(deleted_node)
        if deleted_node.RightChild is not None and deleted_node.LeftChild is not None:
            node_succesor = self.FinMinMax(deleted_node.RightChild, FindMax=False)
            self.copy_key_val(to_node=deleted_node, from_node=node_succesor)
            if node_succesor.is_leaf():
                return self.remove_node_from_parent(node_succesor)
            self.copy_key_val(to_node=node_succesor, from_node=node_succesor.RightChild)
            return self.remove_node_from_parent(node_succesor.RightChild)
        new_node = None
        if deleted_node.RightChild is not None:
            new_node = deleted_node.RightChild
        if deleted_node.LeftChild is not None:
            new_node = deleted_node.LeftChild
        self.copy_key_val(to_node=deleted_node, from_node=new_node)
        return self.remove_node_from_parent(new_node)

    def copy_key_val(self, to_node, from_node):
        to_node.NodeKey = from_node.NodeKey
        to_node.NodeValue = from_node.NodeValue

    def remove_node_from_parent(self, node):
        if node.Parent is None:
            self.Root = None
            return True
        if node is node.Parent.LeftChild:
            node.Parent.LeftChild = None
        if node is node.Parent.RightChild:
            node.Parent.RightChild = None
        node.Parent = None
        return True

    def Count(self):
        if self.Root is None:
            return 0
        count = 1

        left_child_tree = BST(self.Root.LeftChild)
        right_child_tree = BST(self.Root.RightChild)
        count += left_child_tree.Count()
        count += right_child_tree.Count()

        return count
