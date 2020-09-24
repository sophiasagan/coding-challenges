

'''

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

- we could do this recusively, need some kind of backtracking

- how long are the paths going to be?
- each path is cgoing to be n +m -2
-and each point we can only go r or d 

- why is dp a good approach
- we're revisiting polaces
- probably a lot of common subproblems
- w're onlhy movin in one direction each tiem and then we're doing the same thing

- whic means we can us a cach
- we're looking for permutations / 'all possible ways'
'''

# recursively
def uniquePaths_helper(m, n, cache):
    cache = {}
    if m == 1 and n == 1:
        return 1 # base case

    if (m,n) in cache:
        return cache[(m, n)]

    num_down = num_right = 0

    if m > 1: # get the number of paths if we go down
        num_down = uniquePaths_helper(m - 1, n, cache)


    if n > 1:
        num_right = uniquePaths_helper(m, n-1, cache)

    num_path =  num_right + num_down
    cache[(m,n)] = num_path
    return num_path

return uniquePaths_helper(m, n, {})


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # we could to this recursively, need some kind of backtracking
        # How long are the paths going to be? 
        # each path is going to be n + m - 2
        # and each point we can only go r or d
        # Why is DP a good approach? 
        # We're revisiting places
        # probably a lot of common subproblems
        # we're only moving in one direction each time and then we're doing the same thing
        # which means we can use a cache
        # we're looking for permutations / "all possible ways" 
        num_rows = m
        num_cols = n
        # Iteratively 
        cache = [[0 for _ in range(num_cols)] for _ in range(num_rows)]  # cache[i][j] contains the number of paths from i, j to the finish
        cache[num_rows - 1][num_cols - 1] = 1
        for row in range(num_rows - 1, -1, -1): 
            for col in range(num_cols - 1, -1, -1): 
                if row == num_rows - 1 and col == num_cols - 1: 
                    continue
                num_down = num_right = 0
                if row < num_rows - 1: 
                    num_down = cache[row+1][col]
                if col < num_cols - 1: 
                    num_right = cache[row][col+1]
                num_paths = num_right + num_down
                cache[row][col] = num_paths
        return cache[0][0]
        # Recursive w/ memoization
#         def uniquePaths_helper(m, n, cache): 
#             # what's the base case? 
#             if m == 1 and n == 1: 
#                 return 1
#             if (m, n) in cache: 
#                 return cache[(m, n)]
#             num_down = 0
#             num_right = 0
#             # what's the recursive definition? 
#             # if we can go down: 
#             if m > 1: 
#             # get the number of paths if we go down
#                 num_down = uniquePaths_helper(m - 1, n, cache)
#             # if we can go right: 
#             if n > 1: 
#             # get the number of paths if we go right
#                 num_right = uniquePaths_helper(m, n-1, cache)
#             num_paths = num_right + num_down
#             cache[(m, n)] = num_paths
#             return num_paths
#         return uniquePaths_helper(m, n, {})
       