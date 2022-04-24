class Queue2Stack(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)

    def dequeue(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        
        return self.outstack.pop()

q = Queue2Stack()

for i in range(5):
    q.enqueue(i)

print(q.dequeue())
print(q.dequeue())
print(q.enqueue(6))
print(q.enqueue(7))
for i in range(5):
    print(q.dequeue())
