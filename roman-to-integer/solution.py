class Solution:
    def romanToInt(self, s: str) -> int:
        "III"
        lookup =  {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        for i in range(0, len(s)):
            if i == len(s)-1:
                result += lookup[s[i]]
            else:
                if lookup[s[i]] < lookup[s[i+1]]:
                    result -= lookup[s[i]]
                else:
                    result += lookup[s[i]]
        return result

s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))