class Solution:
    def twoSum(self, nums, target):
        ht = {} # init dict
        if not nums: # base case
            return []
        for key, num in enumerate(nums): # iterate and add counter
            if ht.get(target - num) is not None: # get value - 
                return [key, ht.get(target - num)]
            ht[num] = key
        