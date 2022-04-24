'''Requirements for Binary Search Tree
1. All the nodes organized in certain fashion and which also makes them searchable is a Binary Search Tree.
2. Every node of the tree should have a key and a value just like a Dictionary. In this data structure we should be able to traverse the tree both upwards and downwards from any node by using Doubly Linked Lists. So every node should have a link to it's parent as well as to it's children(Left and Right).
3. Left node should be less than parent and Right node should be greater than parent.
4. User should be able to use the indexing operator on the binary search tree object to set or get keys & values.
5. Any node can be searched by keys, deleted by keys and replaced by nodes, keys and values.
6. Insertion Logic: Check if tree is empty or not. If empty then the 1st node added will be root node. If not empty then newly created node will be set in either left child or right child.
7. If data > key(data) of current node then leftchild of that node = key(data) else rightchild of the node = key(data). Before setting data to left child or right child, we check if they are empty or not. If empty, create and assign a new node under left or right child else we will recurse the insert function.
8. Search Operation Logic: Compare if root node's key = data then print a message or return True. Next, if data < root key then check if left subtree exists or not. If it exists then search by recursing search function else print a msg that the key was not found. Same applies for right subtree.
9. Deletion Operation Logic: Check if tree is empty or not. If empty print a msg and stop the execution. If not empty then check if the data <(left) or >(right) root key. Check if the node(left or right) is present. If node is present then recurse the delete function using it's left or right child and assign to itself else print that the given node was not found. For deletion, there are 3 states:
9.i. If the node has 0 children(leaf node) then you delete that child and make the link to it's parent node as None.
9.ii. If there is one child then that child will replace it's parent.
9.iii. If there are both children then you can either replace the greatest value in right subtree with the parent or smallest value in the left subtree with the parent.
10. For the 1st two conditions: If lchild is None then assign to to rchild, make self = none and return temp. Same goes for rchild == None.
11. For last condition, Replace the parent node with, node with  largest key in left subtree OR Replace the parent node with, node with smallest key in right subtree.''' 
class TreeNode:

    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value 
        self.parent = parent
        self.leftchild = left
        self.rightchild = right

    def HasLeftChild(self):
        return self.leftchild
    
    def HasRightChild(self):
        return self.rightchild

    def IsLeftChild(self):
        return self.parent and self.parent.leftchild == self

    def IsRightChild(self):
        return self.parent and self.parent.rightchild == self

    def IsRoot(self):
        return not self.parent

    def IsLeaf(self):
        return not (self.rightchild or self.leftchild)

    def HasAnyChild(self):
        return self.rightchild or self.leftchild

    def HasBothChild(self):
        return self.leftchild and self.rightchild
    
    def ReplaceNode(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.leftchild = lc
        self.rightchild = rc
        if self.HasLeftChild():
            self.leftchild.parent = self
        if self.HasRightChild():
            self.HasRightChild.parent = self

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._put(key, value, self.root)
        self.size += 1

    def _put(self, key, value, currentnode):
        if key < currentnode.key:
            if currentnode.HasLeftChild():
                self._put(key, value, currentnode.leftchild)
            else:
                currentnode.leftchild = TreeNode(key, value, currentnode)

        elif key > currentnode.key:
            if currentnode.HasRightChild():
                self._put(key, value, currentnode.rightchild)
            else:
                currentnode.rightchild = TreeNode(key, value, currentnode)
        else:
            currentnode.value = value

    def InOrder(self, currentnode):
        if currentnode != None:
            print("Key: ",currentnode.key, "Value: ", currentnode.value)
            print("Left <--")
            self.InOrder(currentnode.leftchild)
            print("Right -->")
            self.InOrder(currentnode.rightchild)

    def show(self):
        self.InOrder(self.root)

    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentnode):
        if not currentnode:
            return None
        elif key == currentnode.key:
            return currentnode
        elif key < currentnode.key:
            return self._get(key, currentnode.leftchild)
        else:
            return self._get(key, currentnode.rightchild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodetoremove = self._get(key, self.root)
            if nodetoremove:
                self.remove(nodetoremove)
                self.size -= 1
            else:
                raise KeyError("There is no such key in the tree!")
        if self.size == 1 and key == self.root.key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("There is no such key in the tree!")

    

b = BinarySearchTree()      
b.put(1, 'yellow')
b.put(2, 'red')
b.put(5, 'blue')
b.put(3, 'purple')
b.put(4, 'green')
b.show()