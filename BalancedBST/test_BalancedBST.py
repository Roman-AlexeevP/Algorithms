from BalancedBST import BSTNode, BalancedBST


def test_tiny_balanced_tree():
    tree = BalancedBST()

    sorted_array = [1, 2, 3]

    tree.GenerateTree(sorted_array)

    # assert tree.IsBalanced(tree.Root)
    assert tree.Root is not None
    assert tree.Root.NodeKey == 2
    assert tree.Root.Level == 0

    assert tree.Root.LeftChild.NodeKey == 1
    assert tree.Root.LeftChild.Level == 1
    assert tree.Root.RightChild.NodeKey == 3
    assert tree.Root.RightChild.Level == 1
    assert tree.WideAllNodes() == (2, 1, 3)

def test_one_element_tree():
    tree = BalancedBST()

    sorted_array = [1]
    tree.GenerateTree(sorted_array)
    assert tree.WideAllNodes() == (1, )

def test_non_symmetrical_tree():
    tree = BalancedBST()

    sorted_array = [10, 25, 30, 50, 65, 75, 85, 95]

    tree.GenerateTree(sorted_array)

    assert tree.WideAllNodes() == (50, 25, 75, 10, 30, 65, 85, 95)
