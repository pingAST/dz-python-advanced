class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack пустой")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


stack = Stack()

print(stack.is_empty())  # Выведет True

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.size())  # Выведет 3

print(stack.peek())  # Выведет 3
print(stack.pop())   # Выведет 3
print(stack.pop())   # Выведет 2

print(stack.size())  # Выведет 1

