
def twoSum(nums, target):
    ht = {} # init dict
    if not nums: # base case
        return []
    for key, num in enumerate(nums): # iterate and add counter
        if ht.get(target - num) is not None: # get value - 
            return [key, ht.get(target - num)]
        ht[num] = key
        
# nums = [2, 7, 11, 15]
# target = 9
print(twoSum([1, 2], 3))
print(twosum([6, 2, 1, 7, 11, 15], 7))

print(twosum([2, 7, 11, 15], 9))

print(twosum([0, 4, 3, 0], 3))

print(twosum([-3,4,3,9], 0))