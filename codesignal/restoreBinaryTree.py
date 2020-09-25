'''
Let's define inorder and preorder traversals of a binary tree as follows:

Inorder traversal first visits the left subtree, then the root, then its right subtree;
Preorder traversal first visits the root, then its left subtree, then its right subtree.
For example, if tree looks like this:

    1
   / \
  2   3
 /   / \
4   5   6
then the traversals will be as follows:

Inorder traversal: [4, 2, 1, 5, 3, 6]
Preorder traversal: [1, 2, 4, 3, 5, 6]
Given the inorder and preorder traversals of a binary tree t, but not t itself, restore t and return it.
----

function takes in preorder and inorder information and 
recreates tree from given information
'''

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def restoreBinaryTree(inorder, preorder):
    if not preorder:
        return None
    
    root = Tree(preorder[0]) # root is first element of preorder

    i = inorder.index(preorder[0]) # inorder starts with left and will go to root which will be the first index of preorder

    root.left = restoreBinaryTree(inorder[:i], preorder[1:i+1]) # recursive calls to calculate left branch
    root.right = restoreBinaryTree(inorder[i +1:], preorder[i+1:]) # recursive call to calc right branch

    return root


result = restoreBinaryTree([4, 2, 1, 5, 3, 6], [1, 2, 4, 3, 5, 6])

print(result.value) #1
print(result.left.value) #2
print(result.right.value) #3