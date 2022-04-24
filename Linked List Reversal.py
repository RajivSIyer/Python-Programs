class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

def Reverse(head):

    current = head
    previous_node = None
    next_node = None
    while current:
        next_node = current.next
        current.next = previous_node
        previous_node = current
        current = next_node 
    
    return previous_node

def show(head):
    current = head
    while current.next != None:
        print(current.value)
        current = current.next
    print(current.value)

show(a)
Reverse(a)
show(d)
