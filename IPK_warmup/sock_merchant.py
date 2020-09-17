# hackerrank.com - sock merchant - warmup - difficulty: easy

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # if there's only one sock - you can't sell a single sock

    # increment counter of pairs

    # loop
    # sock_count = {}
    sock_count = set()
    num_pairs = 0

    for sock_color in ar:
        if sock_color in sock_count:
            num_pairs += 1
            sock_count.remove(sock_color)
        else:
            # sock_count[sock_color] = 1 # doesn't matter what value
            sock_count.add(sock_color)

    return num_pairs

    # if i is in hashtable, then +1 to pairs and remove key fromt he hashtable

    # if i is not in hashtable, add it

    # could also work with a set


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


# if there is only one sock we can't sell a pair
# n = number of socks
# ar = colors

# 9 socks
# 10 20 20 10 10 30 50 10 20 colors

# 10(4), 20(3), 30(1), 50(1)

# increment a counter for each pair - hit even
# we need to return total number of matching pairs


