import pytest

from BST import BST, BSTFind, BSTNode


@pytest.fixture()
def tree_for_all_nodes():
    root = BSTNode(parent=None, key=10, val=10)
    tree = BST(root)
    tree.AddKeyValue(15, 15)
    tree.AddKeyValue(5, 5)
    tree.AddKeyValue(12, 12)
    tree.AddKeyValue(17, 17)
    tree.AddKeyValue(11, 11)
    tree.AddKeyValue(13, 13)
    tree.AddKeyValue(16, 16)
    tree.AddKeyValue(18, 18)
    tree.AddKeyValue(2, 2)
    tree.AddKeyValue(6, 6)
    tree.AddKeyValue(1, 1)
    tree.AddKeyValue(3, 3)
    return tree


@pytest.fixture()
def empty_find_result():
    expected_result = BSTFind()
    expected_result.Node = None
    expected_result.NodeHasKey = False
    expected_result.ToLeft = False
    return expected_result


@pytest.fixture()
def tree_with_root():
    root = BSTNode(parent=None, key=1, val=1)
    tree = BST(root)
    return tree, root


def test_FindNodeByKey(tree_with_root):
    tree, root = tree_with_root
    expected_result = BSTFind()
    expected_result.Node = root
    expected_result.NodeHasKey = True
    expected_result.ToLeft = False

    result = tree.FindNodeByKey(1)

    assert result.Node == expected_result.Node
    assert result.NodeHasKey == expected_result.NodeHasKey
    assert result.ToLeft == expected_result.ToLeft


def test_FindNodeByKey_empty_root(empty_find_result):
    tree = BST(node=None)

    result = tree.FindNodeByKey(1)

    assert result.Node == empty_find_result.Node
    assert result.NodeHasKey == empty_find_result.NodeHasKey
    assert result.ToLeft == empty_find_result.ToLeft


def test_FindNodeByKey_empty_key(tree_with_root, empty_find_result):
    tree, root = tree_with_root

    result = tree.FindNodeByKey(None)

    assert result.Node == empty_find_result.Node
    assert result.NodeHasKey == empty_find_result.NodeHasKey
    assert result.ToLeft == empty_find_result.ToLeft


def test_FindNodeByKey_add_left(tree_with_root):
    tree, root = tree_with_root

    expected_result = BSTFind()
    expected_result.Node = root
    expected_result.NodeHasKey = False
    expected_result.ToLeft = True

    real_result = tree.FindNodeByKey(-1)

    assert real_result.Node == expected_result.Node
    assert real_result.NodeHasKey == expected_result.NodeHasKey
    assert real_result.ToLeft == expected_result.ToLeft


def test_FindNodeByKey_add_right(tree_with_root):
    tree, root = tree_with_root

    expected_result = BSTFind()
    expected_result.Node = root
    expected_result.NodeHasKey = False
    expected_result.ToLeft = False

    real_result = tree.FindNodeByKey(100)

    assert real_result.Node == expected_result.Node
    assert real_result.NodeHasKey == expected_result.NodeHasKey
    assert real_result.ToLeft == expected_result.ToLeft

    right_child = BSTNode(parent=root, val=2, key=2)
    root.RightChild = right_child
    expected_result.Node = right_child
    real_result = tree.FindNodeByKey(100)

    assert real_result.Node == expected_result.Node
    assert real_result.NodeHasKey == expected_result.NodeHasKey
    assert real_result.ToLeft == expected_result.ToLeft


def test_AddKeyValue_empty_tree():
    tree = BST(None)
    assert tree.AddKeyValue(1, 1)
    assert tree.Root is not None
    find_result = tree.FindNodeByKey(1)

    assert find_result.Node is not None
    assert find_result.NodeHasKey


def test_AddKeyValue_right(tree_with_root):
    tree, root = tree_with_root

    NEW_KEY, NEW_VALUE = 2, 2
    assert tree.AddKeyValue(NEW_KEY, NEW_VALUE)
    assert root.LeftChild is None
    assert root.RightChild is not None
    assert root.RightChild.NodeValue == NEW_VALUE

    find_result = tree.FindNodeByKey(NEW_KEY)

    assert find_result.Node is not None
    assert find_result.NodeHasKey
    assert find_result.Node.NodeValue == NEW_VALUE


def test_AddKeyValue_left(tree_with_root):
    tree, root = tree_with_root

    NEW_KEY, NEW_VALUE = -5, -5
    assert tree.AddKeyValue(NEW_KEY, NEW_VALUE)
    assert root.RightChild is None
    assert root.LeftChild is not None
    assert root.LeftChild.NodeValue == NEW_VALUE

    find_result = tree.FindNodeByKey(NEW_KEY)

    assert find_result.Node is not None
    assert find_result.NodeHasKey
    assert find_result.Node.NodeValue == NEW_VALUE


def test_FinMinMax_root_min_max(tree_with_root):
    tree, root = tree_with_root
    MIN_VALUE, MAX_VALUE = -50, 50
    for i in range(MIN_VALUE, MAX_VALUE + 1):
        tree.AddKeyValue(i, i)
    assert tree.FinMinMax(root, FindMax=False).NodeKey == MIN_VALUE
    assert tree.FinMinMax(root, FindMax=True).NodeKey == MAX_VALUE


def test_FinMinMax_node_min_max(tree_with_root):
    tree, root = tree_with_root
    root.NodeKey = 10
    root.NodeValue = 10

    MIN_VALUE, MAX_VALUE = 1, 19
    for i in range(MIN_VALUE, MAX_VALUE + 1):
        if i == 10:
            continue
        tree.AddKeyValue(i, i)
    assert tree.FinMinMax(root, FindMax=True).NodeKey == MAX_VALUE
    assert tree.FinMinMax(root, FindMax=False).NodeKey == MIN_VALUE
    tree.AddKeyValue(4.5, 4.5)
    from_node = tree.FindNodeByKey(5).Node

    assert tree.FinMinMax(from_node, FindMax=True).NodeKey == 9
    assert tree.FinMinMax(from_node, FindMax=False).NodeKey == 4.5


def test_DeleteNodeByKey_leaf_root(tree_with_root):
    tree, root = tree_with_root
    assert tree.DeleteNodeByKey(1)
    assert tree.Count() == 0


def test_DeleteNodeByKey_leaf(tree_with_root):
    tree, root = tree_with_root
    tree.AddKeyValue(2, 2)

    assert tree.DeleteNodeByKey(2)
    assert tree.Count() == 1
    assert tree.Root.RightChild is None
    assert tree.Root.LeftChild is None


def test_DeleteNodeByKey_with_left_child(tree_with_root):
    tree, root = tree_with_root
    tree.AddKeyValue(3, 3)
    tree.AddKeyValue(2, 2)
    assert tree.DeleteNodeByKey(3)

    assert tree.Count() == 2
    assert tree.FindNodeByKey(2).Node.LeftChild is None
    assert tree.FindNodeByKey(2).Node.RightChild is None


def test_DeleteNodeByKey_with_right_child(tree_with_root):
    tree, root = tree_with_root
    tree.AddKeyValue(3, 3)
    tree.AddKeyValue(4, 4)
    assert tree.Count() == 3
    assert tree.FindNodeByKey(3).Node.RightChild.NodeValue == 4
    assert tree.FindNodeByKey(3).Node.LeftChild is None

    assert tree.DeleteNodeByKey(3)

    assert tree.Count() == 2
    assert tree.Root.RightChild.NodeKey == 4
    assert tree.FindNodeByKey(4).Node.LeftChild is None
    assert tree.FindNodeByKey(4).Node.RightChild is None


def test_DeleteNodeByKey_with_both_children(tree_with_root):
    tree, root = tree_with_root
    root.NodeKey, root.NodeValue = 10, 10

    tree.AddKeyValue(15, 15)
    tree.AddKeyValue(12, 12)
    tree.AddKeyValue(16, 16)

    assert tree.DeleteNodeByKey(15)
    assert tree.Count() == 3
    assert root.RightChild.NodeValue == 16
    assert root.RightChild.LeftChild is not None and root.RightChild.LeftChild.NodeValue == 12


def test_DeleteNodeByKey_with_both_children_not_leaf(tree_with_root):
    tree, root = tree_with_root
    root.NodeKey, root.NodeValue = 10, 10

    tree.AddKeyValue(15, 15)
    tree.AddKeyValue(12, 12)
    tree.AddKeyValue(20, 20)
    tree.AddKeyValue(16, 16)
    tree.AddKeyValue(17, 17)

    assert tree.DeleteNodeByKey(15)
    assert tree.Count() == 5
    assert root.RightChild.NodeValue == 16
    assert tree.FindNodeByKey(20).Node.LeftChild.NodeValue == 17


def test_Count(tree_with_root):
    tree, root = tree_with_root

    assert tree.Count() == 1


def test_Count_empty():
    tree = BST(None)

    assert tree.Count() == 0


def test_Count_with_children(tree_with_root):
    tree, root = tree_with_root

    for i in range(2, 101):
        assert tree.AddKeyValue(i, i)
    assert tree.Count() == 100


def test_WideAllNodes(tree_for_all_nodes):
    tree = tree_for_all_nodes

    all_nodes = tree.WideAllNodes()

    assert [10, 5, 15, 2, 6, 12, 17, 1, 3, 11, 13, 16, 18] == [node.NodeKey for node in all_nodes]


def test_WideAllNodes(tree_with_root):
    tree, root = tree_with_root

    tree.AddKeyValue(2, 2)
    tree.AddKeyValue(3, 3)
    tree.AddKeyValue(-1, -1)
    all_nodes = tree.WideAllNodes()

    assert [1, -1, 2, 3] == [node.NodeKey for node in all_nodes]


def test_DeepAllNodes_inorder(tree_for_all_nodes):
    tree = tree_for_all_nodes

    all_nodes = tree.DeepAllNodes(0)

    assert [1, 2, 3, 5, 6, 10, 11, 12, 13, 15, 16, 17, 18] == [node.NodeKey for node in all_nodes]


def test_DeepAllNodes_postorder(tree_for_all_nodes):
    tree = tree_for_all_nodes

    all_nodes = tree.DeepAllNodes(1)

    assert [1,3,2,6,5,11,13,12,16,18,17,15,10] == [node.NodeKey for node in all_nodes]


def test_DeepAllNodes_preorder(tree_for_all_nodes):
    tree = tree_for_all_nodes

    all_nodes = tree.DeepAllNodes(2)

    assert [10, 5, 2, 1, 3, 6, 15, 12, 11, 13, 17, 16, 18] == [node.NodeKey for node in all_nodes]

