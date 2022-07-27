from Heap import Heap


def test_buildHeap():
    heap = Heap()
    heap.MakeHeap([1, 2, 3], 1)
    assert heap.HeapArray == [3, 1, 2]


def test_buildHeap_large_size():
    heap = Heap()
    array = [49, 14, 93, 64, 25, 80, 69, 60, 1, 91, 3, 98, 26]
    heap_array = [98, 91, 93, 60, 64, 80, 69, 14, 1, 25, 3, 49, 26, None, None]
    heap.MakeHeap(array, 3)
    assert heap.HeapArray == heap_array
    assert heap.GetMax() == 98

