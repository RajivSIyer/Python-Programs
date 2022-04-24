class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)

#It is Cyclical
a.next_node = b
b.next_node = c
c.next_node = a

x = Node(1)
y = Node(2)
z = Node(3)

#Not Cyclical
x.next_node = y
y.next_node = z

def cyclical_check(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:

        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker1 == marker2:
            return True

    return False

print(cyclical_check(a))
print(cyclical_check(x))