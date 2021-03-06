from SimpleTree import SimpleTree, SimpleTreeNode

def test_AddChild():
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    child: SimpleTreeNode = SimpleTreeNode(5, None)
    tree: SimpleTree = SimpleTree(parent)
    tree.AddChild(parent, child)
    assert child in tree.Root.Children and child.Parent is parent

def test_GetAllNodes():
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    tree: SimpleTree = SimpleTree(parent)
    child: SimpleTreeNode = SimpleTreeNode(5, None)
    tree.AddChild(parent, child)
    siblings = [SimpleTreeNode(i, None) for i in range(5)]
    for sibling in siblings:
        tree.AddChild(child, sibling)
    all_nodes = [parent, child] + siblings
    tested_all_nodes = tree.GetAllNodes()
    for node in all_nodes:
        assert node in tested_all_nodes
    assert len(tested_all_nodes) == 7

def test_GetAllNodesOneElement():
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    tree: SimpleTree = SimpleTree(parent)
    assert len(tree.GetAllNodes()) == 1 and parent in tree.GetAllNodes()
    child: SimpleTreeNode = SimpleTreeNode(5, None)
    tree.AddChild(parent, child)
    all_nodes = tree.GetAllNodes()
    assert len(all_nodes) == 2 and child in all_nodes and parent in all_nodes

def test_FindNodesByValue():
    value = 5
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    tree: SimpleTree = SimpleTree(parent)
    first_child: SimpleTreeNode = SimpleTreeNode(value, None)
    second_child = SimpleTreeNode(value, None)
    tree.AddChild(parent, first_child)
    tree.AddChild(parent, second_child)
    nodes = [first_child, second_child]
    for node in nodes:
        assert node in tree.FindNodesByValue(value)

def test_Count():
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    tree: SimpleTree = SimpleTree(parent)
    child: SimpleTreeNode = SimpleTreeNode(5, None)
    tree.AddChild(parent, child)
    assert tree.Count() == 2


def test_CountMultiple():
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    tree: SimpleTree = SimpleTree(parent)
    nodes = [tree.AddChild(parent, SimpleTreeNode(i, None)) for i in range(100)]
    assert tree.Count() == 101

def test_DeleteNode():
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    child: SimpleTreeNode = SimpleTreeNode(2, None)
    tree: SimpleTree = SimpleTree(parent)
    tree.AddChild(parent, child)
    nodes = [tree.AddChild(child, SimpleTreeNode(i, None)) for i in range(100)]
    tree.DeleteNode(child)
    assert tree.Count() == 1


def test_LeafCount():
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    child: SimpleTreeNode = SimpleTreeNode(2, None)
    tree: SimpleTree = SimpleTree(parent)
    tree.AddChild(parent, child)
    assert tree.LeafCount() == 1

def test_LeafCountZero():
    tree: SimpleTree = SimpleTree(None)
    assert tree.LeafCount() == 0

def test_GetAllNodesWithLevel():
    parent: SimpleTreeNode = SimpleTreeNode(1, None)
    tree: SimpleTree = SimpleTree(parent)
    child: SimpleTreeNode = SimpleTreeNode(5, None)
    tree.AddChild(parent, child)
    siblings = [SimpleTreeNode(i, None) for i in range(5)]
    for sibling in siblings:
        tree.AddChild(child, sibling)
    print("\n")
    print(tree.GetAllNodesWithLevel())