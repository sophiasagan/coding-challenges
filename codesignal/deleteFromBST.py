#
'''
A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Removing a value x from a BST t is done in the following way:

If there is no x in t, nothing happens;
Otherwise, let t' be a subtree of t such that t'.value = x.
If t' has a left subtree, remove the rightmost node from it and put it at the root of t';
Otherwise, remove the root of t' and its right subtree becomes the new t's root.


Delete value node from  a binary tree and preserve BST property.
    - Traverse the tree to find the node to delete;
    - If found:
        1) Node has no children, just return None to the caller (which set
        its left/right node to the returned None)
        2) Node has one child, just return the child to the caller (which set
        its left/right node to the returned child and thus detach the node to delete)
        3) Node has both children:
           - Find the max in left subtree (min in right subtree would work too)
           - Make the value of the node to delete as the max just found
           - Remove the above duplicated node from the subtree
           - Return the root of the subtree, which now doesn't contain the deleted node
'''

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def max_node(t):
    while t and t.right:
        t = t.right
    return t

def clearNode(t):
    left = t.left
    right = t.right
    if left == None and right == None:
        return None
    elif left == None:
        return right
    else:
        if left.right == None:
            left.right = right
            return t.left
        previous = t
        t = t.left
        while t.right != None:
            previous = t
            t = t.right
        previous.right = t.left
        t.left = left
        t.right = right
    return t

def deleteNode(t, value):
    if t == None:
        return None # base case

    if t.value == value:  
        return clearNode(t)

    if t.value > value: # value node is in left subtree
        t.left = deleteNode(t.left, value)

    elif t.value < value: # value node is in right subtree
        t.right = deleteNode(t.right, value)
        
    else:
        if not t.left and not t.right: # no children
            return None
        elif not t.left: # no left child
            return t.right
        elif not t.right: # no right child
            return t.left
        else:
            max_left = max_node(t.left) # find max left node
            t.value = max_left.value # clone value into node
            t.left = deleteNode(t.left, max_left.value) # set cloned node to left subtree head - remove cloned node
    return t
    
       
def deleteFromBST(t, queries):
    for val in queries:
        t = deleteNode(t, val)
    return t

# passing 10/12


# def deleteNode(t):
    left = t.left
    right = t.right
    if left == None and right == None:
        return None
    elif left == None:
        return right
    else:
        if left.right == None:
            left.right = right
            return t.left
        previous = t
        t = t.left
        while t.right != None:
            previous = t
            t = t.right
        previous.right = t.left
        t.left = left
        t.right = right
    return t


# def deleteOneFromBST(t, value):
    if t == None:
        return None
    if t.value == value:  
        return deleteNode(t)
    if value < t.value:
        if t.left == None:
            return t
        else:
            t.left = deleteOneFromBST(t.left, value)
    else:
        if t.right == None:
            return t
        else:
            t.right = deleteOneFromBST(t.right, value)
    return t


def deleteFromBST(t, queries):
    for value in queries:
        t = deleteOneFromBST(t, value)
    return t