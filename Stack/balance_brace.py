from Stack import Stack

def is_balanced_string(string: str) -> bool:
    stack = Stack()
    for brace in string:
        last = stack.peek()
        if last == '(' and brace == ')':
            stack.pop()
            continue
        stack.push(brace)
    return stack.size() == 0
