def count_words(sentence):
    ht = {} # init dict
    for words in sentence.split(): # iterate through sentence and split into sep words
        if words not in ht: # check for word in dict
            ht[words] = 0 # add word to dict with count of 0
        ht[words] += 1 # else update count

    return ht 

