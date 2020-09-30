
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

    target = count - k # represents the number from the beginning of the array
    
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


def remove_kth_element_from_end(head, k):
    count = 0 
    curr = head

    while curr:
        count += 1
        curr = curr.next

    # reset 
    target = count - k
    curr_node = 0
    curr = head
    prev = head
    
    while curr_node != target:
        prev = curr
        curr = curr.next

        # iterate
        curr_target += 1
    if prev:
        prev.next = curr.next

    else:
        # shift head by 1
        head = head.next
    return head


# since we cannot remove from the list from the back we need
# to count the total of the linked lists values and subtract k 
# to find our target to remove. 

def remove_kth_element_from_end(head, k):
    count = 0
    curr_node = head

    # iterate through the list and count the number of nodes
    while curr_node is not None:
        curr_node = curr_node.next
        count += 1 
    # once we have the number of nodes we we can get the target by subtracting the num of nodes minus k
    target = count - k

    prev = None
    pointer = head
    
    # previous pointer is going to be one behind the curr pointer
    # previous will point the previous node that we want to remove
    while target != 0: # find k - node to remove
        prev = pointer
        pointer = pointer.next
        count -= 1

    # remove the node
    if prev is None:
        return head.next

    else:
        prev.next = pointer.next
        pointer.next = None
        return head


# traversed list twice once to get count and once to remove
# time O(n+n) = O(n)
# space O(1)