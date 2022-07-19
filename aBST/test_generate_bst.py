import generate_bst


def test_GenerateBBSTArray():
    balanced_tree_arr = [2, 1, 3]
    unsorted_arr = [3, 2, 1]
    assert generate_bst.GenerateBBSTArray(unsorted_arr) == balanced_tree_arr


def test_GenerateBBSTArray_large():
    balanced_tree_arr = [10, 5, 15, 4, 6, 12, 16]
    unsorted_arr = [16, 15, 10, 12, 5, 4, 6]
    assert generate_bst.GenerateBBSTArray(unsorted_arr) == balanced_tree_arr
