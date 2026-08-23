import ctypes
import math


class Vector:
    def __init__(self, capacity=16):
        if capacity < 16:
            capacity = 16

        self._capacity = 2 ** math.ceil(math.log2(capacity))
        self._size = 0

        self._array = (ctypes.c_int * self._capacity)()

    def _ptr_at(self, index):
        base_address = ctypes.addressof(self._array)
        element_size = ctypes.sizeof(ctypes.c_int)

        address = base_address + index * element_size

        return ctypes.cast(
            address,
            ctypes.POINTER(ctypes.c_int)
        )

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def is_empty(self):
        return self._size == 0

    def at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._ptr_at(index).contents.value

    def find(self, item):
        for i in range(self._size):
            if self.at(i) == item:
                return i

        return -1

    def push(self, item):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        self._ptr_at(self._size).contents.value = item

        self._size += 1

    def insert(self, index, item):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._size, index, -1):
            self._ptr_at(i).contents.value = (
                self._ptr_at(i - 1).contents.value
            )

        self._ptr_at(index).contents.value = item

        self._size += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty vector")

        item = self._ptr_at(self._size - 1).contents.value

        self._size -= 1

        self._ptr_at(self._size).contents.value = 0

        if (
            self._size <= self._capacity // 4
            and self._capacity // 2 >= 16
        ):
            self._resize(self._capacity // 2)

        return item

    def delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        for i in range(index, self._size - 1):
            self._ptr_at(i).contents.value = (
                self._ptr_at(i + 1).contents.value
            )

        self._size -= 1

        self._ptr_at(self._size).contents.value = 0

        if (
            self._size <= self._capacity // 4
            and self._capacity // 2 >= 16
        ):
            self._resize(self._capacity // 2)

    def remove(self, item):
        i = 0

        while i < self._size:
            if self.at(i) == item:
                self.delete(i)
            else:
                i += 1

    def _resize(self, new_capacity):
        new_array = (ctypes.c_int * new_capacity)()

        for i in range(self._size):
            new_array[i] = self._ptr_at(i).contents.value


        self._array = new_array
        self._capacity = new_capacity

if __name__ == "__main__":
    v = Vector(capacity=16)

    print(f"   is_empty(): {v.is_empty()}")
    print(f"   size(): {v.size()}, capacity(): {v.capacity()}")

    print("\n2. Thêm phần tử")
    v.push(10)
    v.push(20)
    v.prepend(5)
    print(f"   Kích thước hiện tại: {v.size()}")
    print(f"   {[v.at(i) for i in range(v.size())]}")
    print("\n3. Truy xuất và tìm kiếm")
    print(f"   Phần tử tại index 0: {v.at(0)}")
    print(f"   Vị trí của giá trị 20: {v.find(20)}")
    print(f"   Vị trí của giá trị 99: {v.find(99)}")

    print("\n4. Chèn phần tử")
    v.insert(1, 15)
    print(f"   Giá trị tại index 1 sau khi insert: {v.at(1)}")
    print(f"   {[v.at(i) for i in range(v.size())]}")

    print("\n5. Thêm trùng lặp")
    v.push(15)
    print(f"   Tìm thấy 15 đầu tiên tại: {v.find(15)}")
    print(f"   {[v.at(i) for i in range(v.size())]}")

    v.remove(15)
    print(f"   Kích thước sau khi remove: {v.size()}")
    print(f"   Tìm 15 sau khi remove: {v.find(15)}")
    print(f"   {[v.at(i) for i in range(v.size())]}")

    print("\n6. Xóa phần tử")
    val_pop = v.pop()
    print(f"   Giá trị vừa pop(): {val_pop}")
    v.delete(0)
    print(f"   Phần tử duy nhất còn lại tại 0: {v.at(0)}")
    print(f"   Kích thước cuối cùng: {v.size()}")
