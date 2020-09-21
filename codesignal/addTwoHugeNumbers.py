# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    nums_a = 0
    nums_b = 0
    str_a = ""
    str_b = ""

    while a is not None:
        nums_a += 1
        str_a += str(a.value).zfill(4) # zfill -> fill with 0s
        a = a.next

    while b is not None:
        nums_b += 1
        str_b += str(b.value).zfill(4)
        b = b.next

    sum_all = str(int(str_a) + int(str_b))

    temp=[sum_all[::-1][i:i+4] for i in range(0, len(sum_all[::-1]), 4)]

    total = []
    for i in temp:
        total.append(int(i[::-1]))
    total = total[::-1]
    return total
