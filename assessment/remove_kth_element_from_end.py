
def remove_kth_element_from_end(head, k):
# if the k is 0
    count = 0
    curr = head
    
    while (curr.next):
        curr = curr.next
        count += 1
        
    count += 1
    
    if k > count:
        return head
    if k == 0:
        return head

    target = count - k
    
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