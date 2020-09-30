# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        curr = head

        while (curr.next):
            curr = curr.next
            count += 1

        count += 1

        if n > count:
            return head
        if n == 0:
            return head

        target = count - n

        if target == 0:
            return head.next

        prev = head
        curr = head
        new_count = 1

        while (curr.next and new_count <= target):
            prev = curr
            curr = curr.next
            new_count += 1

        prev.next = curr.next

        return head
        