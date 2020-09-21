# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

'''
    Approach:
    1. Edge case: n == 0, just return the list.
    2. Establish nodes for head, last, and previous (one before start).
    3. Edge case: If n is the length of the list, return the list.
    4. Iterate through the list until we find the last, updating head, last, and previous.
    5. Clean up by setting the next node for end and previous.
'''
def rearrangeLastN(l, n):

    if n == 0:
        return l
    
    head = l # this is what we return
    last = l # this will be connected to l, the original linked list, before the return
    prev = 1 # this tracks the node right before the start of the new list
    count = 1

    while count < n:
        last = last.next
        count += 1

    if last.next == None:
        return l

    while last.next is not None:
        if last.next is not None:
            last = last.next
            prev = head
            head = head.next

    last.next = l
    prev.next = None
    return head