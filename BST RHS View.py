'''
                1
        2               3
    4       5       6       7
8

[1,3,7,8]'''

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None

def BSTRightView(root):
    result = []
    queue = [root]
    level = []

    while queue != [] and root != None:
        for node in queue:
            if node.lchild:
                level.append(node.lchild)
            if node.rchild:
                level.append(node.rchild)
        result.append(node.value)
        queue = level
        level = []
    return result

def BSTLeftView(root):
    result = []
    queue = [root]
    level = []

    while queue != [] and root != None:
        for node in queue:
            if node.rchild:
                level.append(node.rchild)
            if node.lchild:
                level.append(node.lchild)
        result.append(node.value)
        queue = level
        level = []
    return result

root = BinaryTreeNode(1)
root.lchild = BinaryTreeNode(2)
root.rchild = BinaryTreeNode(3)
root.lchild.lchild = BinaryTreeNode(4)
root.lchild.rchild = BinaryTreeNode(5)
root.rchild.lchild = BinaryTreeNode(6)
root.rchild.rchild = BinaryTreeNode(7)
root.lchild.lchild.lchild = BinaryTreeNode(8)

print(BSTRightView(root))
print(BSTLeftView(root))      