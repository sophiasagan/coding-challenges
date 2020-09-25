'''
Is t2 a subtree in t1 
Return true or false
'''
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
    if t2 is None:
        return True
    if t1 is None:
        return False
    
    if isEqual(t1, t2):
        return True

    return isSubtree(t1.left, t2) | isSubtree(t1.right, t2) # try left and right subtree


def isEqual(t1, t2):
    if not t1 and not t2: # base case
        return True
    if not t1 or not t2:
        return False
    
    return (t1.value == t2.value and isEqual(t1.left, t2.left) and isEqual(t1.right, t2.right))
    


