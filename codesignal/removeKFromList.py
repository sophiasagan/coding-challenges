# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):

    while l!=None and l.value == k:
        l = l.next

    temp = l

    while temp:
        prev = temp
        temp = temp.next
        while temp and (temp.value == k):
            temp = temp.next
        prev.next = temp

    return l

