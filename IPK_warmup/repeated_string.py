# hackerrank.com - repeated string - difficulty: easy

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # I know how many times n appears in s
    num_as_in_s = 0
    for char in s:
        if char == 'a':
            num_as_in_s += 1

    # I know the length of s, so I can figure out how many times s is repeated in the substring
    full_repetitions_of_s = n // len(s)
    #multiply the number f times s is repeated * the number of times a appears in s
    remainder_length = n % len(s)
    num_as_in_remainder = 0
    remainder_string = s[0:remainder_length]
    for char in remainder_string:
        if char == 'a':
            num_as_in_remainder += 1
    num_as_in_substring = full_repetitions_of_s * num_as_in_s + num_as_in_remainder
    # I need to handle the "remainder" that's left over
    return num_as_in_substring
    # Brute Force:
    # substring = ""
    # while len(substring) < n:
    #     substring += s
    # substring = substring[0:n] # chop off the extra letters on substring so it's n characters long
    # print(len(substring), substring)

    # num_As = 0
    # for char in substring:
    #     if char == "a":
    #         num_As += 1
    # return num_As

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
