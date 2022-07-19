def GenerateBBSTArray(a):
    if len(a) == 0:
        return []
    array = sorted(a)
    return built_bst(array, 0, len(array) - 1)


def built_bst(array, left, right):
    if left > right or not array:
        return []
    middle = left + (right - left) // 2
    result = [array[middle], ]
    result += built_bst(array, left, middle - 1)
    result += built_bst(array, middle + 1, right)
    return result
