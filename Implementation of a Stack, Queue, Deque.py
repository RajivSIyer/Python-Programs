'''class Stack(object):

    def __init__(self):
        self.items = []
    
    def IsEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

s = Stack()
print(s.IsEmpty())
print(s.push(1))
print(s.push(2))
print(s.peek())
print(s.size())
print(s.push(3))
print(s.pop())
print(s.IsEmpty())
print(s.clear())
print(s.IsEmpty())'''

'''class Queue(object):

    def __init__(self):
        self.items = []
    
    def IsEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

q = Queue()
print(q.enqueue(4))
print(q.enqueue('sample'))
print(q.enqueue(True))
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.clear())
print(q.IsEmpty())'''

class Deque(object):

    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    def AddFront(self, item):
        self.items.insert(0, item)

    def AddRear(self, item):
        self.items.append(item)

    def RemoveFront(self):
        return self.items.pop(0)

    def RemoveRear(self):
        return self.items.pop(-1)

    def size(self):
        return len(self.items)

    def __str__(self):
        return ("The list is:" + str(self.items))

d = Deque()
print(d.AddFront(1))
print(d.AddRear(5))
print(d.AddRear(4))
print(d)
print(d.RemoveFront())
print(d.RemoveFront())
print(d)
print(d.AddFront(3))
print(d.AddRear(2))
print(d)
print(d.RemoveRear())
print(d.RemoveRear())
print(d.size())
