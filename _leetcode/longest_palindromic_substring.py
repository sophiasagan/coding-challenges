class Solution(object):    
    def longestPalindrome(self, s): 
        if len(s) == 1: 
            return s
        if len(s) == 2: 
            # it's either of the form "aa" or "ax"
            if s[0] == s[-1]: 
                # "aa"
                return s
            # "ab", return a character arbitrarily
            return s[0]
        table = [[False for _ in s] for _ in s]
# Maintain a boolean table[n][n] that is filled in bottom up manner.
# The value of table[i][j] is true, if the substring from i to j inclusive is palindrome, otherwise false.
# To calculate table[i][j], check the value of table[i+1][j-1], if the value is true and str[i] is same as str[j], then we make table[i][j] true.
# Otherwise, the value of table[i][j] is made false.
        # initialize len 1: 
        for i in range(0, len(s)): 
            # substring of length 1 is always a palindrome
            table[i][i] = True
            if i < len(s) - 1: 
                # Substring of length 2 
                table[i][i+1] = s[i] == s[i+1]            
        # Have to build up the table starting with the shortest substrings first and going bigger
        for substring_length in range(2, len(s)): 
            # consider substrings of length 3+
            for i in range(0, len(s) - substring_length):
                j = i + substring_length
                is_substring = (s[i] == s[j]) and table[i+1][j-1]
                table[i][j] = is_substring
        # find the longest in this table
        longest = ""
        for i in range(0, len(s)): 
            for j in range(len(s) - 1, i - 1, -1):
                if table[i][j]: 
                    substring = s[i:j+1]
                    if len(substring) > len(longest): 
                        longest = substring
        return longest
    palindrome_cache = {}
    def is_palindrome(self, s): 
        # were reversing the given substring and if it 
        # matches the given string we return true
        # if the first and last char match and the inner bit is a palindrome
        if s in self.palindrome_cache: 
            return self.palindrome_cache[s]
        if len(s) <= 1: 
            return True
        result = (s[0] == s[-1] and self.is_palindrome(s[1:-1]))
        self.palindrome_cache[s] = result
        return result
    def longestPalindrome_v1(self, s):
        """
        :type s: str
        :rtype: str
        """
        # We might want a helper function to tell if a substring is a palindrome or not
            # an implementation for the helper function is to reverse and compare
        # we need a variable to hold the current longest substring
        # split the string into all substrings and test those with the helper func?
        # brute force ^
        if len(s) == 1: 
            return s
        longest_palindrome = ""
        all_substring = []
        for substring_length in range(len(s), -1, -1): 
            for i in range(len(s) - substring_length + 1): 
                substring = s[i: i+substring_length]
                all_substring.append(substring)
        for substring in all_substring: 
            if self.is_palindrome(substring): 
                if len(substring) > len(longest_palindrome): 
                    return substring
        return longest_palindrome

###### Josh's Sliding Window solution:Start with window size = length of the input string and check if palindrome, if not, decrement the window size, and check all substrings of that length- If substring is palindrome, return the substring.. if no palindrome found for that window size, decrement window size again and repeat. Iterate until palindrome found, or window size is 1 (When window size reaches 1, just return the first character of the input string)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        def is_pal(x):
            return x == x[::-1]
        window_size = len(s)
        while window_size > 1:
            for i in range(len(s) - window_size + 1): 
                substring = s[i : i + window_size]
                if is_pal(substring):
                    return substring
            window_size -= 1
        return s[0]

###### Vlad's Solution
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        output = odd = 0
        count = collections.Counter(s)
        for c in count:
            output += count[c]
            if count[c] % 2 == 1:
                output -= 1
                odd += 1
        return output + bool(odd)

#### David's Solution

def longestPalindrome(self, s: str) -> str:
    str_len = len(s)
    p_table = [[0 for col in range(str_len)] for row in range(str_len)]
    # incrementally build up a lookup table, starting
    # with str len 1, up to 3 or more
    # Length 1
    max_len = 1
    idx = 0
    while idx < str_len:
        p_table[idx][idx] = True
        idx += 1
    # Length 2
    idx, start = 0, 0
    while idx < str_len - 1:
        if s[idx] == s[idx + 1]:
            p_table[idx][idx + 1] = True
            start = idx
            max_len = 2
        idx += 1
    # Length 3+
    pal_len = 3  # initialize palindrome len to 3, then work up to length str_len
    while pal_len <= str_len:
        idx = 0
        # Check substring of increasing size to see if they're a palindrome
        # Adjust the max_len if a larger palindromic substring is encountered
        while idx < (str_len - pal_len + 1):
            # Increment the length of the substring to test for pallandrome
            end = idx + pal_len - 1
            # Test if substr from index idx+1 to index-1 end is a pallandrome
            # and if the larger substring from idx to end is also a pallandrome
            if (p_table[idx + 1][end - 1] and s[idx] == s[end]):
                p_table[idx][end] = True
                if pal_len > max_len:
                    max_len = pal_len
                    start = idx
            idx += 1
        pal_len += 1
    return s[start: start + max_len]