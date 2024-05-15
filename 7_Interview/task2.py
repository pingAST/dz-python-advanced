from task1 import Stack


def is_balanced(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    brackets_map = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or stack.peek() != brackets_map[char]:
                return "Несбалансированно"
            stack.pop()

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


# Примеры проверки
print(is_balanced("(((([{}]))))"))  # Сбалансированно
print(is_balanced("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(is_balanced("{{[()]}}"))  # Сбалансированно
print(is_balanced("}{"))  # Несбалансированно
print(is_balanced("{{[(])]}}"))  # Несбалансированно
print(is_balanced("[[{())}]"))  # Несбалансированно
