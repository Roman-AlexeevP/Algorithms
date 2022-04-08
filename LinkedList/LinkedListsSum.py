from LinkedList import Node, LinkedList

def compare_lists(first_list: LinkedList, second_list:LinkedList) -> bool:
    return first_list.len() == second_list.len()

def sum_two_list(first_list: LinkedList, second_list:LinkedList) -> LinkedList:
    if compare_lists(first_list, second_list):
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
