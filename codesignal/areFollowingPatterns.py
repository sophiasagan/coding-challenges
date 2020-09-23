def areFollowingPatterns(strings, patterns):

    '''
    if the string follows the pattern then true
    if the string doesn't follow the pattern false
    verify string an pattern are same lenghth = base case
    set dict
    loop through string for words 
    loop through pattern for assigned pattern
    compare return true or false
    '''
    if len(strings) != len(patterns):
        return False

    ht = {}

    for i in range(len(strings)):
        if patterns[i] not in ht:
            if strings[i] not in ht.values():
                ht[patterns[i]] = strings[i]
            else:
                return False

        elif ht[patterns[i]] != strings[i]:
            return False
    return True
