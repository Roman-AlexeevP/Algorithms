class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children: list = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None or NewChild is None:
            return None
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is None:
            return None
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        deleted_tree = SimpleTree(NodeToDelete)
        for child in NodeToDelete.Children:
            deleted_tree.DeleteNode(child)


    def GetAllNodes(self):
        if self.Root is None:
            return []
        nodes = [self.Root, ]
        for children in self.Root.Children:
            child_tree = SimpleTree(children)
            nodes += child_tree.GetAllNodes()
        return nodes

    def GetAllNodesWithLevel(self, prev_level=None):
        if self.Root is None:
            return []
        level = prev_level or 1
        print(f"{self.Root} on level: {level} with value: {self.Root.NodeValue}")
        level += 1
        for children in self.Root.Children:
            child_tree = SimpleTree(children)
            child_tree.GetAllNodesWithLevel(level)


    def FindNodesByValue(self, val):
        if self.Root is None:
            return []
        nodes = []
        if self.Root.NodeValue == val:
            nodes.append(self.Root)
        for children in self.Root.Children:
            child_tree = SimpleTree(children)
            nodes += child_tree.FindNodesByValue(val)
        return nodes


    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        if self.Root is None:
            return 0
        count = 1
        for child in self.Root.Children:
            child_tree = SimpleTree(child)
            count += child_tree.Count()
        return count


    def LeafCount(self):
        if self.Root is None:
            return 0
        if not self.Root.Children:
            return 1
        count = 0
        for child in self.Root.Children:
            child_tree = SimpleTree(child)
            count += child_tree.LeafCount()
        return count

    def EvenTrees(self):
        result_list = []
        if self.Root is None:
            return result_list
        for child in self.Root.Children:
            child_tree = SimpleTree(child)
            child_tree_count = child_tree.Count()
            if child_tree_count % 2 == 0 and child_tree_count > 1:
                result_list.append(self.Root)
                result_list.append(child)


        return result_list

