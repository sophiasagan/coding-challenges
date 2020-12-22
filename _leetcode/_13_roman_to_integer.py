class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        _sum = 0
        for i in range(len(s)):
            value = roman[s[i]]
            # If the next number is larger number, this value is negative
            if i+1 < len(s) and roman[s[i+1]] > value:
                _sum -= value
            else: 
                _sum += value
        return _sum
            
        