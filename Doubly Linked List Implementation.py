class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next = b
b.prev = a

b.next = c
c.prev = b

print(a.next.value)
print(b.prev.value)
print(b.next.value)
print(c.prev.value)