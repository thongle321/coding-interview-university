class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def size(self):
        return self._size

    def __repr__(self):
        items = []
        current_item = self.top

        while current_item is not None:
            items.append(str(current_item.data))
            current_item = current_item.next
        return ', '.join(items)

    def empty(self):
        return self.top is None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        data = self.top.data
        self.top = self.top.next

        self._size -= 1
        return data

    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.data


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(4)
    stack.push(15)
    stack.push(6)

    print(stack)

    print("Peek: ", end="")
    print(stack.peek())

    print("Pop: ", end="")
    print(stack.pop())
    print(stack)
