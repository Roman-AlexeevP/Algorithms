from LinkedList import Node, LinkedList


def sum_two_list(first_list: LinkedList, second_list:LinkedList) -> LinkedList:
    is_equal = first_list.len() == second_list.len()
    if is_equal:
        node_first_list = first_list.head
        node_second_list = second_list.head
        result_list = LinkedList()

        while node_first_list is not None and node_second_list is not None:
            new_node = Node(node_second_list.value+node_first_list.value)
            result_list.add_in_tail(new_node)
            node_second_list = node_second_list.next
            node_first_list = node_first_list.next
        return result_list
    return None
