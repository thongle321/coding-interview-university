# Implement using Linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def size(self):
        return self._size

    def __repr__(self):
        items = []
        current_item = self.front
        while current_item is not None:
            items.append(str(current_item.data))
            current_item = current_item.next
        return ', '.join(items)

    def enqueue(self, data):
        node = Node(data)

        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self._size += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError('Queue is empty')
        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._size -= 1
        return data

    def empty(self):
        return self.front is None

# Implement using fixed-sized array
class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self._size = 0
        self.front = 0
        self.rear = 0

    def empty(self):
        return self._size == 0

    def full(self):
        return self._size == self.capacity

    def enqueue(self, data):
        if self.full():
            raise IndexError("Queue is full")

        self.items[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        self._size += 1

    def dequeue(self):
        if self.empty():
            raise IndexError("Queue is empty")

        data = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self._size -= 1

        return data

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    print(queue)
    print(queue.size())

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue)
    print(queue.size())

    q = QueueArray(5)

    print("Empty:", q.empty())

    print("\nEnqueue 10")
    q.enqueue(10)
    print(q.items)

    print("\nEnqueue 20")
    q.enqueue(20)
    print(q.items)

    print("\nEnqueue 30")
    q.enqueue(30)
    print(q.items)

    print("\nDequeue:", q.dequeue())
    print(q.items)

    print("\nDequeue:", q.dequeue())
    print(q.items)

    print("\nEnqueue 40")
    q.enqueue(40)
    print(q.items)

    print("\nEnqueue 50")
    q.enqueue(50)
    print(q.items)

    print("\nEnqueue 60")
    q.enqueue(60)
    print(q.items)

    print("\nFull:", q.full())

    print("\nDequeue:", q.dequeue())
    print(q.items)

    print("\nDequeue:", q.dequeue())
    print(q.items)

    print("\nEmpty:", q.empty())
