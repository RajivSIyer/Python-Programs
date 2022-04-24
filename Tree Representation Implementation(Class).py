class BinaryTree(object):
    def __init__(self, obj):
        self.key = obj
        self.LeftChild = None
        self.RightChild = None

    def InsertLeftChild(self, obj):

        if self.LeftChild == None:
            self.LeftChild = BinaryTree(obj)
        else:
            t = BinaryTree(obj)
            t.LeftChild = self.LeftChild
            self.LeftChild = t

        return self.LeftChild

    def InsertRightChild(self, obj):

        if self.RightChild == None:
            self.RightChild = BinaryTree(obj)
        else:
            t = BinaryTree(obj)
            t.RightChild = self.RightChild
            self.RightChild = t
        
        return self.RightChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def getLeftChild(self):
        return self.LeftChild

    def getRightChild(self):
        return self.RightChild

def PreOrder(tree): #Key Left Right (KLR)
    if tree != None:
        print(tree.getRootVal())
        PreOrder(tree.getLeftChild())
        PreOrder(tree.getRightChild())

def InOrder(tree): #Left Key Right (LKR)
    if tree != None:
        InOrder(tree.getLeftChild())
        print(tree.getRootVal())
        InOrder(tree.getRightChild())

def PostOrder(tree): #Left Right Key (LRK)
    if tree != None:
        PostOrder(tree.getLeftChild())
        PostOrder(tree.getRightChild())
        print(tree.getRootVal())   

'''
            a

    b               c

d       e       f       g
'''
a = BinaryTree('a')
print(a.getRootVal())
print(a.InsertLeftChild('b').InsertLeftChild('d'))
print(a.getLeftChild().InsertRightChild('e'))
print(a.InsertRightChild('c').InsertLeftChild('f'))
print(a.getRightChild().InsertRightChild('g'))

print('This is PRE-ORDER: ')
PreOrder(a)
print('This is IN-ORDER: ')
InOrder(a)
print('This is POST-ORDER: ')
PostOrder(a)