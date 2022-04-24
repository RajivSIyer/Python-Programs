class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

def nth_to_last_node(n, head):
    if n <= 0:
        raise Exception('Invalid Input!')

    node_array = []
    current = head
    link_count = 0
    while current:
        link_count += 1
        if len(node_array) == n:
            node_array = node_array[1:]
        node_array.append(current)
        current = current.next_node

    if n > link_count:
        raise Exception('Not enough Nodes to return n.')
        
    return node_array[0]

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

try:
    target_value = nth_to_last_node(0,a)
    if target_value != None:
        print(target_value.value)

except Exception as E:
    print(E)
