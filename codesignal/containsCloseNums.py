def containsCloseNums(nums, k):

    '''
    are there duplicate numbers k indices apart?
    '''

    if len(nums) <= 1:
        return False    

    ht = {}

    for key, value in enumerate(nums):
        if value in ht and key - ht[value] <= k:
            return True
        ht[value] = key

    return False
