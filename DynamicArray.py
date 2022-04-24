import ctypes
import sys

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.MakeArray(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if 0 <= k < self.n:
            return self.A[k]
        return IndexError("Out of bounds index.")

    def append(self, d):
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = d
        self.n += 1

    def _resize(self, new_cap):
        
        B = self.MakeArray(new_cap)

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_cap

    def MakeArray(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def __str__(self):
        s = '['
        for i in range(self.n):
            s = s + str(self.A[i])
            if i < (self.n-1):
                s = s + ','
        s += ']' 
        return s

    def cap(self):
        return self.capacity

arr = DynamicArray()

print(arr.cap())
print(sys.getsizeof(arr))
arr.append(11)
print(sys.getsizeof(arr))

print(arr.cap())
arr.append(21)
print(sys.getsizeof(arr))

print(arr.cap())
arr.append(31)
print(sys.getsizeof(arr))

print(arr)

print(len(arr))

print(arr[1])

print(arr.cap())
arr.append([1,2,3])
print(sys.getsizeof(arr))

print(arr)

print(len(arr))