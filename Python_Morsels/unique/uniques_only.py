def uniques_only(arr):
    return list(set(arr))
    # sets are unordered - arr should be return in same order but dupes removed

def uniques_only(arr):
    items = []
    for i, item in enumerate(arr):
        if item not in arr[:i]:
            items.append(item)
    return items
# Here we're slicing the sequence that comes into our function to get all items before our current one (the i-th one). This allows us to check whether an item appeared before our current item.
# only works on sequences though

def uniques_only(arr):
    items = []
    for item in arr:
        if item not in items:
            items.append(item)
    return items
    # works but slow for large lists

def uniques_only(arr):
    seen = set()
    items = []
    for item in iterable:
        if item not in seen:
            items.append(item)
            seen.add(item)
    return items
    # Sets rely on hashes for lookups so containment checks won't slow down as our hash grows in size. Notice we're building up both a list and a set but we're checking only the set for containment and returning only the list. We still need to make a list in addition to our set because sets are unordered by nature and we want the order of first appearance of each item to be maintained.

def uniques_only(arr):
    return dict.fromkeys(arr).keys()

# This is a somewhat clever and hacky solution. It's short, but it's not very clear. It also only works on Python 3.6+. I prefer the set solution from a readability standpoint, but the dict.fromkeys solution is likely faster.



# Bonus #1
# Let's try tackling the first bonus.

def uniques_only(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            yield item
            seen.add(item)
# We're using a generator function here. Generator functions are unlike regular functions. They return a generator object which will return items every time a yield statement is hit in our generator function.

# We can't turn this generator function into a generator expression because we need to add items to our set as we iterate, which isn't possible with a generator expression.

# Bonus #2
# Let's talk about the second bonus now.

# If we want our function to work with non-hashable types, we'll need to use something besides a set or a dictionary to store seen values. We could use a list, like we did before:

def uniques_only(iterable):
    seen = []
    for item in iterable:
        if item not in seen:
            yield item
            seen.append(item)
# This works, but it will be slower. Answering the question "item not in seen" when using a list requires iterating all the way through the list looking for a match. A set can answer the same question without iterating at all.

# Bonus #3
# If we want to tackle the third bonus problem and make our code continue to work efficiently for hashable types, we could check each item to see if it's hashable:

from collections.abc import Hashable

def uniques_only(iterable):
    seen_hashable = set()
    seen_unhashable = []
    for item in iterable:
        if isinstance(item, Hashable):
            if item not in seen_hashable:
                yield item
                seen_hashable.add(item)
        else:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)

# The collections.abc.Hashable type uses duck typing when doing an isinstance check, so asking isinstance(item, Hashable) will always give us the correct answer for each object in Python.

# Another way we could check for hashability is to simply try to add each item to the set and if it fails, add it to the list instead:

def uniques_only(iterable):
    seen_hashable = set()
    seen_unhashable = []
    for item in iterable:
        try:
            if item not in seen_hashable:
                yield item
                seen_hashable.add(item)
        except TypeError:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)

# This is practicing "it's easier to practice forgiveness than permission", which is a common programming practice in the Python world. The exception handling involved does make the non-hashable case a bit slower though, so that if statement might be better overall depending on what we're optimizing for.

