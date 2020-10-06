# def is_anagram(word1, word2):
#     word1, word2 = word1.lower(), word2.lower() # ignore case
#     return sorted(word1) == sorted(word2) # if letters in word1 and letters of word2 are equivalent return True

# Bonus 1

# from collections import Counter


# def is_anagram(word1, word2):
#     """Return True if the given words are anagrams."""
#     word1, word2 = word1.lower(), word2.lower()
#     return Counter(word1.replace(' ', '')) == Counter(word2.replace(' ', '')) # remove spaces

# Bonus 2

# def is_anagram(word1, word2):
    # """Return True if the given words are anagrams."""
    # word1, word2 = word1.lower(), word2.lower()
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # letters1 = sorted(c for c in word1 if c in alphabet)
    # letters2 = sorted(c for c in word2 if c in alphabet)
    # return letters1 == letters2

# Strings in Python have an isalpha method that returns True if the given string is entirely alphabetical. We can use this to select just the alphabetical characters as we loop over our string:

# def is_anagram(word1, word2):
    # """Return True if the given words are anagrams."""
    # word1, word2 = word1.lower(), word2.lower()
    # letters1 = sorted(c for c in word1 if c.isalpha())
    # letters2 = sorted(c for c in word2 if c.isalpha())
    # return letters1 == letters2

# Knowing methods on Python's built-in types can come in handy sometimes. We could take this a step further by making the sorting lines into a function that we call twice:

# def letters_in(string):
    # """Return sorted list of letters in given string."""
    # return sorted(
    #     char
    #     for char in string.lower()
    #     if char.isalpha()
    # )

# def is_anagram(word1, word2):
    # """Return True if the given words are anagrams."""
    # return letters_in(word1) == letters_in(word2)
# We were doing the same operation on both words so moving this logic into a separate functions makes sense for clarity.

# If we use a Counter object we could rename our letters_in function to counter_letters, which might be more clear:

# from collections import Counter
 
# def count_letters(string):
#     """
#     Return sorted list of letters in given string.
#     """
#     return Counter(
#         char
#         for char in string.lower()
#         if char.isalpha()
#     )

# def is_anagram(word1, word2):
#     """
#     Return True if the given words are anagrams.
#     """
#     return count_letters(word1) == count_letters(word2)

# Bonus 3

import unicodedata

def remove_accents(string):
    """Return decomposed form of the given string."""
    return unicodedata.normalize('NFKD', string)

def letters_in(string):
    """Return sorted list of letters in given string."""
    string = remove_accents(string.lower())
    return sorted(
        char
        for char in string
        if char.isalpha()
    )

def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return letters_in(word1) == letters_in(word2)

    # We'll need to normalize our unicode data to such that characters are decomposed into parts (so accents are treated separately from the character they accent). If we look up unicode normalization or search for how to ignore accent marks in unicode strings we'll find NFKD form. The unicodedata module can help us normalize our strings into NFKD form (NFD form should work as well):
#     Notice our is_anagram function hasn't changed at all here. We've added a remove_accents function and we're now calling it on our lowercased string in our letters_in function.

# You may have noticed that NFD form passes the tests just as well as NFKD form. If you use NFKD form, alternative versions of letters pass too though:

# >>> is_anagram("ℍ𝕖𝕝𝕝𝕠", "hello")
# True
# This wasn't explicitly required by the bonus, but NFKD makes this equivalence possible. We would however have to change the order of our lower() method calls because "ℍ𝕖𝕝𝕝𝕠".lower() == "ℍ𝕖𝕝𝕝𝕠" which means we'll end up with "Hello" if we lowercase and then normalize. You can play with that if you're interested, but you likely won't need to worry about this distinction so I wouldn't recommend going down a unicode manipulation rabbit hole right now. Save that for another day.
# https://en.wikipedia.org/wiki/Unicode_equivalence#Normal_forms