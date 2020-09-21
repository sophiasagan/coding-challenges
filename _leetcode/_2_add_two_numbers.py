# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = res_head = ListNode(0) # init current node to head of return list
        carry = 0 # init carry to zero

        while l1 or l2 or carry: # while there's a value for l2, l1, or carry
            val1 = 0 
            val2 = 0
            if l1:
                val1 = l1.val # init val1 to head of l1
                l1 = l1.next
            if l2:
                val2 = l2.val # init val2 to head of l2
                l2 = l2.next

            sum = val1 + val2 + carry # sum like normal addition
            carry = 0 
            if sum > 9:
                sum = sum % 10
                carry = 1 # overflow
            result.next = ListNode(sum)
            result = result.next
        if carry != 0:
            result.next = ListNode(carry)
        return res_head.next # return res next node
