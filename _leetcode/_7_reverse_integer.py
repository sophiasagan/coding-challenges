class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x > 0:
            res = int(str(x)[::-1])
        if x < 0:
            res = int(("-" + str(x * -1)[::-1]))
        if res <= -2**31 or res >= 2**31:
            return 0
        else:
            return res


# initial solution
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        return str(x)[::-1]


Input:
-123
Output:
321-
Expected:
-321

# second working solution


class Solution:
    def reverse(self, x: int) -> int:

        if x >= 0:
            x = str(x)
            return str(x)[::-1]
        if x < 0:
            x = x * -1
            x = str(x)
            return int((str(x)[::-1]))*-1


Input:
120
Output:
021
Expected:
21

# 3rd


class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2**31 or x >= 2**31:
            return 0

        if x >= 0:
            x = str(x)
            return int(str(x)[::-1])
        if x < 0:
            x = x * -1
            x = str(x)
            return int((str(x)[::-1]))*-1


Input:
1534236469
Output:
9646324351
Expected:
0
