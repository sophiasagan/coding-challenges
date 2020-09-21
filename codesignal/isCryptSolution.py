# def valid_crypt(str):
#     if len(str) > 1 and str[0] == "0":
#         return False
#     return True

def digit_string(str, hash):
    return ''.join([hash[x] for x in str])

def isCryptSolution(crypt, solution):
    ht = {} # decoder

    for kv in solution:
        ht[kv[0]] = kv[1]
    # return ht

    digit_strings = [digit_string(x, ht) for x in crypt]

    for str in digit_strings:
        if len(str) > 1 and str[0] == "0":
            return False
    
    n = [int(x) for x in digit_strings]

    return(n[0] + n[1] == n[2])

