'''
You have two arrays of strings, words and parts. Return an array that contains the strings from words, modified so that any occurrences of the substrings from parts are surrounded by square brackets [], following these guidelines:

If several parts substrings occur in one string in words, choose the longest one. If there is still more than one such part, then choose the one that appears first in the string.

Example

For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", "mel", "lon", "el", "An"], the output should be
findSubstrings(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"].

While "Watermelon" contains three substrings from the parts array, "a", "mel", and "lon", "mel" is the longest substring that appears first in the string.

-----
Trie is an efficient information reTrieval data structure. 
Using Trie, search complexities can be brought to optimal limit (key length). 
If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, 
where M is maximum string length and N is number of keys in tree. 
Using Trie, we can search the key in O(M) time. 
However the penalty is on Trie storage requirements (Please refer Applications of Trie for more details)
Every node of Trie consists of multiple branches. 
Each branch represents a possible character of keys. 
We need to mark the last node of every key as end of word node. 

'''


class TrieNode:
    def __init__(self, alpha):
        self.alpha = alpha
        self.is_word = False
        self.child = {}

    def insert(self, word):
        curr_node = self
        for alpha in word:
            if alpha not in curr_node.child:
                curr_node.child[alpha] = TrieNode(alpha)
            curr_node = curr_node.child[alpha]
        curr_node.is_word = True



def search(root, word):
    longest_substr = 0
    longest_pos = 0

    for start in range(len(word)):
        curr_node = root

        for position in range(start, len(w)):
            alpha = word[position]
            if alpha not in curr_node.child:
                break
            curr_node = curr_node.child[alpha]
            length = position - start + 1

            if curr_node.is_word and length > longest_substr:
                longest_substr = length
                longest_pos = start
    if longest_substr == 0:
        return word
    end = longest_pos + longest_substr
    return word[:longest_pos] + '[' + word[longest_pos: longest_pos + longest_substr] + ']' + word[end:]
    # count = 0
    # res = -1
    # curr_node = root
    # for i, alpha in enumerate(word):
    #     curr_node = curr_node.child.get(alpha)
    #     if not curr_node:
    #         break
    #     count += 1
    #     if curr_node.is_word:
    #         res = max(res, count)
    # return res
    
def findSubstrings(words, parts):
    root = TrieNode('')

    for p in parts:
        root.insert(p)
    return [search(root, word) for word in words]

    # def parse(w):
    #     initStart = -1
    #     initCount = -1
    #     for start in range(len(w)):
    #         count = trie.search(w[start:])
    #         if count and count > initCount:
    #             initCount = count
    #             initStart = start
    #     return w[:initStart] + '[' + w[initStart:initStart + initCount] + ']' + w[initStart + initCount:]

    # result = []
    # for w in words:
    #     result.append(parse(w))
    # return result


    # https://en.wikipedia.org/wiki/Trie
    # https://www.geeksforgeeks.org/trie-insert-and-search/


    # passing 6 of 9 
# Input:
# words:
# ["Apple", 
#  "Melon", 
#  "Orange", 
#  "Watermelon"]

# parts:
# ["a", 
#  "mel", 
#  "lon", 
#  "el", 
#  "An"]

# Output:
# ["Apple", 
#  "Me[lon]Melon", 
#  "Or[a]Ora", 
#  "Water[mel]Watermel"]

# Expected Output:
# ["Apple", 
#  "Me[lon]", 
#  "Or[a]nge", 
#  "Water[mel]on"]