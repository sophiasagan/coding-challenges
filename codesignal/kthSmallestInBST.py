#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    val = set()

    def traverse(t):
        if t == None:
            return # base case

        val.add(t.value) # add value to set
        traverse(t.left) # traverse left sign of tree
        traverse(t.right) # traverse right side of tree
    
    traverse(t) 

    if len(val) < k:
        return None
    result = sorted(val)

    return result[k-1]



