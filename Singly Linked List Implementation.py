class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

a = Node('a')
b = Node('b')
c = Node('c')

a.nextnode = b
b.nextnode = c

currentnode = a

if currentnode != None:
    while currentnode.nextnode != None:
        print(currentnode.value)
        currentnode = currentnode.nextnode

    print(currentnode.value)
