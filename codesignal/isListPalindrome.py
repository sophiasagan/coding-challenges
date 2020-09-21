# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    arr = [] # convert ll to array
    if(l != None):
        arr.append(l.value)
        curr = l.next
        while curr !=None: # iterate through nodes
            arr.append(curr.value) # append node to array
            curr = curr.next # traverse through the nodes  
    
    for i in range(int(len(arr)/2)):
        if arr[i] != arr[len(arr) - i -1]:
            return False
    return True