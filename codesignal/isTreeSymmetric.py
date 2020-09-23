#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

'''
both side of the tree must mirror each other to return True
'''

def isMirror(lst,rst):
    # at least one node is None
    if not (lst and rst):
        # Two empty trees are mirrors of each other
        if not lst and not rst:
            return True
        # if one is None and the other exits, then the trees are not symmetric
        else:
            return False
    
    elif lst.value == rst.value:
        # the left subtree must be a mirror of the right subtree and visa versa
        return isMirror(lst.left,rst.right) & isMirror(lst.right,rst.left)
    
    else:
        return False
    

def isTreeSymmetric(t):
    if t is None: # base case
        return True
    else: # return mirror
        return isMirror(t.left, t.right)





