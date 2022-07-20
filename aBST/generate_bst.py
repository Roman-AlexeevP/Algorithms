def GenerateBBSTArray(a):
    if len(a) == 0:
        return []
    array = sorted(a)
    new_array = [None]*len(array)
    return build_bst(array, new_array, 0, 0, len(array) - 1)


def build_bst(array, new_array, root, left, right):
    if left > right:
        return []
    middle = left + ((right - left) // 2)
    new_array[root] = array[middle]
    left_root = 2 * root + 1
    build_bst(array, new_array, left_root, left, middle - 1)
    right_root = 2 * root + 2
    build_bst(array, new_array, right_root, middle + 1, right)
    return new_array
