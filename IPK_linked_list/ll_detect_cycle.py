# hackerrank.com - linked lists: detect a cycle - difficulty: easy

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    visited = set()
    # want to keep track of places we've been
    # only go to each place once
    # maybe a visited set?

    # iterate through the linked list
    node = head
    while node is not None:
    # if the node isn't in visited, add it
        if node in visited: 
    # if it is, return True --> there's a cycle
            return True
        else:
            visited.add(node)
        node = node.next
    # if we iterate through thte entire linked list, return False
    return False

    # saving a variabe with previous node, and
    # if the .next is == to prev, 
    # then you have the cycle