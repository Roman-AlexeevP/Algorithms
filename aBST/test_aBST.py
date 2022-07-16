import pytest

from aBST import aBST


def test_find_one_root_empty_tree():
    tree = aBST(depth=0)
    assert tree.FindKeyIndex(key=10) == 0


def test_find_one_root_filled_tree():
    tree = aBST(depth=0)
    assert len(tree.Tree) == 1


    tree.Tree[0] = 0
    assert tree.FindKeyIndex(0) == 0
    assert tree.FindKeyIndex(1000) is None


def test_insert_to_tree():
    tree = aBST(depth=3)
    assert len(tree.Tree) == 15

    assert tree.AddKey(8) == 0
    assert tree.AddKey(4) == 1
    assert tree.AddKey(12) == 2
    assert tree.AddKey(2) == 3
    assert tree.AddKey(6) == 4
    assert tree.AddKey(10) == 5
    assert tree.AddKey(14) == 6
    assert tree.AddKey(1) == 7
    assert tree.AddKey(3) == 8
    assert tree.AddKey(5) == 9
    assert tree.AddKey(7) == 10
    assert tree.AddKey(9) == 11
    assert tree.AddKey(11) == 12
    assert tree.AddKey(13) == 13
    assert tree.AddKey(15) == 14
    assert tree.Tree == [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    assert tree.AddKey(123) == -1


def test_not_fully_filled_tree():
    tree = aBST(depth=2)

    assert tree.AddKey(8) == 0
    assert tree.AddKey(4) == 1
    assert tree.AddKey(12) == 2
    assert tree.AddKey(10) == 5
    assert tree.AddKey(14) == 6
    assert tree.AddKey(2) == 3
    assert tree.AddKey(6) == 4
    assert len(tree.Tree) == 7
    assert tree.Tree == [8, 4, 12, 2, 6, 10, 14]
