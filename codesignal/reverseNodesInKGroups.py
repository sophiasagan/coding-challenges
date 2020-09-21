# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    # if k == 1:
    #     return l
    # next_node = None
    # prev = None
    # curr = l
    # count = k
    # while curr and count != 0:
    #     # curr = curr.next
    #     # curr.next = prev
    #     # prev = curr
    #     # curr = next_node
    #     # count -= 1
    #     next_node == curr.next
    #     curr.next = prev
    #     curr = next_node
    #     count -= 1


    # if next_node:
    #     l.next = reverseNodesInKGroups(next_node, k)
    # return prev

    # passes 10/13
    '''Approach:
    1. If the list is empty, simply return it.
    2. Iterate through the list to find its length. If the list is
    shorter than k, simply return the list.
    3. Create three temporary nodes, current, previous, and next. Swap
    them in place for n iterations. At the end:
    previous: the head of the k chunk list
    current: the tail
    next: current.next
    4. Recursively call the function to return the list.
    '''

    if not l:
        return l

    curr = l
    count = k

    # Decrease until either n is 0 or the list is empty
    while curr and count:
        curr = curr.next
        count -= 1 

    # If the latter, return the list
    if count:
        return l

    curr = l
    prev = None
    next = None
    count = k

    # 3
    while curr and count:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count -= 1

    # 4
    if next:
        l.next = reverseNodesInKGroups(next, k)

    return prev