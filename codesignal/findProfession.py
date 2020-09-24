def findProfession(level, pos):
    '''
    - returns a string "Doctor" | "Engineer"
    - everyone has two children
    - first child of engineer is an engineer and second child is doctor
    - first chilc of doctor is a doctor and second child is an engineer
    - all generations start with engineer

    Since the prefix is always the same for each level, if the
    position is odd, we can recursively simplify the problem by going
    to the next level and halving the position.
    '''
    if level == 1: # root has to be engineer
        return "Engineer"

    # next level has to be Engineer then Doctor
    if level == 2 and pos == 1: 
        return "Engineer"
    if level == 2 and pos == 2:
        return "Doctor"

    # if the position is odd then we are starting with engineer
    if pos % 2 == 1:
        if findProfession(level - 1, (pos+1)/2) == "Engineer":
            return "Engineer"
        else:
            return "Doctor"
    else:
        # if positionis even then assume we are starting with doctor and reverse assignments
        if findProfession(level - 1, pos/2) == "Engineer":
            return "Doctor"
        else:
            return "Engineer"

if __name__ == '__main__':
    level = 3
    pos = 4
    print(findProfession(level, pos))