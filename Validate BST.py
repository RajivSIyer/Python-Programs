def validate(treenode): #Pre-Order Traversal KLR

    if not treenode:
        return False

    if treenode.left:    
        if treenode.left.value < treenode.value:
            res = validate(treenode.left)
        else:
            print("The BST is bad.")
            return False

    if res:
        if treenode.right:
            if treenode.right.value > treenode.value:
                return validate(treenode.right)
            else:
                print("The BST is bad.")
                return False
    else:
        return False

    return True