# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    x = l1
    y = l2

    head = None
    result = None

    if x.value < y.value:
        head = x
        x = x.next

    else:
        head = y
        y = y.next
    result = head

    while x and y:
        if x.value < y.value:
            result.next = x
            x = x.next
        else:
            result.next = y
            y = y.next
        result = result.next

    while y:
        result.next = y
        result = result.next
        y = y.next

    while x:
        result.next = x
        result = result.next
        x = x.next

    return head

    