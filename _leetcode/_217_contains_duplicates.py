

class Solution: # set
    def containsDuplicate(self, nums):

        n = set()

        for num in nums:
            if num not in n: # if numbers in num array are not in set add to set
                n.add(num)
            else: # if number in num array already in set return True as there is a duplicate
                return True
        # if reached this point then there is no duplicates
        return False
