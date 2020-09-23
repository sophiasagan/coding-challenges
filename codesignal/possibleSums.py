def possibleSums(coins, quantity):

    '''
    for each coin given there is a quantity
    how many different sums can be made with the given coins and quantity?
    '''
    ht = set([0]) # init set
    # print(ht)
    # coin_value = 0

    # |= performs an in-place+ operation between pairs of objects. 
    # In particular, between:

    # sets: a union operation
    # dicts: an update operation
    # counters: a union (of multisets) operation
    # numbers: a bitwise OR, binary operation
    # https://stackoverflow.com/questions/3929278/what-does-ior-do-in-python
    for key, value in zip(coins, quantity):    
        ht |= {
            i + choice # existing sum plus the choice
            for choice in range(key, key * value + 1, key) # iterate over range of multiples for this value
            for i in ht} # iterate over all existing sums

        # print(ht)
    return len(ht) - 1 # remove 0 from the set

    # for key, value in zip(coins, quantity):
    #     for i in range(1, quantity[key + 1:]):
    #         coin_value += value
    # return ht

if __name__ == '__main__':
    coins = [10,50,100]
    qty = [1,2,1]
    print(possibleSums(coins, qty))