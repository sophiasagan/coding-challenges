def firstDuplicate(a):
    ht = {}
    for num in a:
        if num not in ht:
            ht[num] = 0
        elif num in ht:
            ht[num] += 1
            return num
    
    return -1

