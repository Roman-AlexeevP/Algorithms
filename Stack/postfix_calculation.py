from Stack import Stack

def calcucate_postfix(expression_stack: Stack) -> int:
    stack_with_numbers = Stack()
    while expression_stack.size() > 0:
        value = expression_stack.pop()
        if value == '=':
            return stack_with_numbers.pop()
        if isinstance(value, int):
            stack_with_numbers.push(value)
            continue
        first_value = stack_with_numbers.pop()
        second_value = stack_with_numbers.pop()
        if value == "+":
            stack_with_numbers.push(first_value+second_value)
            continue
        if value == "*":
            stack_with_numbers.push(first_value*second_value)
            continue
