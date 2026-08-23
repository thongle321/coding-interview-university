import keyword
class HashTable:
    DELETED = object()
    def __init__(self, size = 10):
        self.m = size
        self.table = [None] * size

    def hash(self, k, m=None):
        if m is None:
            m = self.m
        return hash(k) % m

    def add(self, k, v):
        index = self.hash(k)

        for i in range(self.m):
            item = self.table[index]

            if item is None or item is self.DELETED:
                self.table[index] = (k, v)
                return

            if item[0] == k:
                self.table[index] = (k, v)
                return

            index = (index + 1) % self.m

        raise ValueError("Hash table is full")

    def exists(self, k):
        index = self.hash(k)

        for i in range(self.m):
            item = self.table[index]

            if item is None:
                return False

            if item is not self.DELETED and item[0] == k:
                return True

            index = (index + 1) % self.m
        return False

    def get(self, k):
        index = self.hash(k)

        for i in range(self.m):
            item = self.table[index]

            if item is None:
                return None

            if item is not self.DELETED and item[0] == k:
                return item[1]

            index = (index + 1) % self.m
        return None

    def remove(self, k):
        index = self.hash(k)

        for i in range(self.m):
            item = self.table[index]

            if item is None:
                return False

            if item is not self.DELETED and item[0] == k:
                self.table[index] = self.DELETED
                return True

            index = (index + 1) % self.m
        return False

if __name__ == '__main__':
    ht = HashTable(5)

    ht.add("apple", 10)
    ht.add("banana", 20)
    ht.add("orange", 30)

    print(ht.exists("apple"))
    print(ht.exists("grape"))

    print(ht.get("banana"))

    ht.add("banana", 99)
    print(ht.get("banana"))

    ht.remove("banana")
    print(ht.exists("banana"))
    print(ht.get("banana"))
