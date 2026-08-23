class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def value_at(self, index):
        current = self.head
        for i in range(index):
            if current is not None:
                current = current.next
        if current is None:
            raise IndexError("index out of range")

        return current.data

    def push_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self._size += 1

    def pop_front(self):
        if (self.head is None):
            print("List is empty")
        data =  self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def push_back(self, data):
        node = Node(data)
        if self.empty():
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self._size += 1

    def pop_back(self):
        if self._size == 1:
            data = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            data = current.next.data
            current.next = None
        self._size -= 1
        return data

    def front(self):
        return self.head.data

    def back(self):
        return self.value_at(self._size - 1)

    def insert(self, index, data):
        if index == 0:
            self.push_front(data)
            return

        current = self.head
        for i in range(index - 1):
            current = current.next

        node = Node(data)
        node.next = current.next
        current.next = node
        self ._size += 1

    def erase(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self._size -= 1

    def value_n_from_end(self, n):
        current = self.head

        for _ in range (self._size - n):
            current = current.next
        return current.data

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def remove_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is not None:
            current.next = current.next.next
            self._size -= 1

    def traverseList(self, head):
        while head is not None:
            print(head.data, end="")
            if head.next is not None:
                print(" -> ", end="")
            head = head.next
        print()

if __name__ == "__main__":
    ll = LinkedList()

    ll.push_back(5)
    ll.push_back(10)

    print("List: ", end="")
    ll.traverseList(ll.head)

    print("Value at 0: ", end="")
    print(ll.value_at(0))

    print("Push front 15: ", end="")
    ll.push_front(15)
    ll.traverseList(ll.head)

    print("Push back 20: ", end="")
    ll.push_back(20)
    ll.traverseList(ll.head)

    print("Pop back:  ", end="")
    ll.pop_back()
    ll.traverseList(ll.head)

    print("Insert at 2 value 30: ", end="")
    ll.insert(2, 30)
    ll.traverseList(ll.head)

    print("Erase at 2: ", end="")
    ll.erase(2)
    ll.traverseList(ll.head)


    print("Value from end: ", end="")
    print(ll.value_n_from_end(1))

    print("Reverse: ", end="")
    ll.reverse()
    ll.traverseList(ll.head)

    print("Remove value: ", end="")
    ll.remove_value(10)
    ll.traverseList(ll.head)
