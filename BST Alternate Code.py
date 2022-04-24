class BST:
    level = 0
    d = {}

    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key == None:
            self.key = data
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def find(self, data):
        if self.key == data:
            print("Key found!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.find(data)
            else:
                print("Key was not found!")
        else:
            if self.rchild:
                self.rchild.find(data)
            else:
                print("Key was not found!")

    def preorder(self):
        BST.level = 0
        self.__preorder()

    def __preorder(self):

        BST.level += 1
        print("Level:", BST.level, "Self-->", self.key)
        if BST.level not in BST.d:
            BST.d[BST.level] = []
        BST.d[BST.level].append(self.key)

        if self.lchild:
            print("Level:", BST.level, self.key,"-->Left -->")
            self.lchild.__preorder()
            BST.level -= 1
        if self.rchild:
            print("Level:", BST.level, self.key,"-->Right -->")
            self.rchild.__preorder()
            BST.level -= 1
    
    def inorder(self):
        if self.lchild:
            print(self.key,"-->Left -->")
            self.lchild.inorder()
        print("Self-->", self.key)
        if self.rchild:
            print(self.key,"-->Right -->")
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            print(self.key,"-->Left -->")
            self.lchild.postorder()
        if self.rchild:
            print(self.key,"-->Right -->")
            self.rchild.postorder()
        print("Self-->", self.key)

    def delete(self, data, root):
        if self.key == None:
            print("Tree is Empty!")
            return None
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, root)
            else:
                print("Given node is not present!")
                return None
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, root)
            else:
                print("Given node is not present!")
                return None
        else:
            if self.lchild == None:
                temp = self.rchild
                if data == root.key:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    del(temp)
                    return self
                self = None
                return temp
            if self.rchild == None:
                temp = self.lchild
                if data == root.key:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    del(temp)
                    return self
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, root)
        return self

    def minobj(self):
        nodel = self
        while nodel.lchild:
            nodel = nodel.lchild
        return nodel
        
    def minval(self):
        return self.minobj().key
    
    def maxobj(self):
        noder = self
        while noder.rchild:
            noder = noder.rchild
        return noder
        
    def maxval(self):
        return self.maxobj().key


def count(node):
    if node == None:
        return 0
    else:
        return 1 + count(node.lchild) + count(node.rchild)


def validate(treenode): #Pre-Order Traversal KLR
    res = True
    if not treenode:
        return False

    if treenode.lchild:    
        if treenode.lchild.key < treenode.key:
            res = validate(treenode.lchild)
        else:
            print("The BST is bad on left side.")
            return False

    if res:
        if treenode.rchild:
            if treenode.rchild.key > treenode.key:
                return validate(treenode.rchild)
            else:
                print("The BST is bad on right side.")
                return False
    else:
        return False

    return True

def TrimTree(tree, minval, maxval):
    rootnode = tree
    while __TrimTree(tree, minval, maxval, rootnode):
        pass

def __TrimTree(tree, minval, maxval, rootnode):
    if tree.lchild:
        retval = __TrimTree(tree.lchild, minval, maxval, rootnode)
        if retval:
            return True
    if tree.rchild:
        retval = __TrimTree(tree.rchild, minval, maxval, rootnode)
        if retval:
            return True
    if minval <= tree.key <= maxval:
        rootnode.delete(tree.key, rootnode)
        return True
    return False

root = BST(15)
l = [9,10,8,11,16,14,17]
'''
                            15
            9                               16
        8       10                              17
                    11                  
                        14
'''
for i in l:
    root.insert(i)
root.preorder()
print(BST.d)
for i in range(len(BST.d)):
    s = ''
    for j in BST.d[i+1]:
        s += str(j) + '\t'
    print(s)
TrimTree(root,10,15)
root.preorder()
'''print("\n")
root.inorder()
print("\n")
root.postorder()
print("\n")
root.find(15)
print("\n")

if count(root) > 1:
    print(root.delete(10, root))
    print("\n")
    root.preorder()
else:
    print("Single node tree cannot be deleted!")

print(root.maxobj())
print(root.minobj())
print(root.maxval())
print(root.minval())

if validate(root):
    print("Tree is good.")
else:
    print("Tree is bad.")'''

'''
print("\n")
root.delete(10, root)
print("\n")
root.preorder()
print("\n")
root.delete(15, root)
print("\n")
root.preorder()'''

'''root2 = BST(5)
root2.lchild = BST(3)
root2.lchild.lchild = BST(2)
root2.rchild = BST(7)
root2.rchild.lchild = BST(10)
root2.rchild.rchild = BST(9)

if validate(root2):
    print("Tree is good.")
else:
    print("Tree is bad.")'''