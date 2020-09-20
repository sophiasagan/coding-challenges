def rotateImage(a):
    length = len(a) # making our life easier by pulling out this variable and naming it
    result = [[0 for i in range(length)] for j in range(length)] # assigning result to matrix -> matrix should only be as long & wide as matrix in input
    for i in range(length): # iterate through i & j
        for j in range(length):
            newX = j # for new matrix
            newY = length - i - 1 # for new matrix moving it 90 degrees clockwise
            result[newX][newY] = a[i][j] # assigning the new matrix
    return result
    



