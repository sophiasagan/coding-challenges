#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if t == None:
        return False # base case

    sum_goal = s - t.value
    l = False
    r = False

    if t.left == None and t.right == None: # if reach leaf node and sum is 0; return true
        return (sum_goal == 0)

    if t.left != None: # recursive tree - keep going until all nodes are reached
        l = hasPathWithGivenSum(t.left, sum_goal)

    if t.right != None:
        r = hasPathWithGivenSum(t.right, sum_goal)

    return (l | r)

