import generate_bst


def test_GenerateBBSTArray():
    balanced_tree_arr = [2, 1, 3]
    unsorted_arr = [3, 2, 1]
    assert generate_bst.GenerateBBSTArray(unsorted_arr) == balanced_tree_arr


def test_GenerateBBSTArray_medium():
    balanced_tree_arr = [10, 5, 15, 4, 6, 12, 16]
    unsorted_arr = [16, 15, 10, 12, 5, 4, 6]
    assert generate_bst.GenerateBBSTArray(unsorted_arr) == balanced_tree_arr


def test_GenerateBBSTArray_small():
    balanced_tree_arr = [7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]
    unsorted_arr = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert generate_bst.GenerateBBSTArray(unsorted_arr) == balanced_tree_arr
