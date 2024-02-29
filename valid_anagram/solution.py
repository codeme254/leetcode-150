class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        checks if the words in t can be rearranged to form words in s
        i.e checks if t is an anagram of s

        Args:
          s: input string
          t: input string
        
        Returns:
          true if t is an anagram of s and false otherwise
        """
        if len(s) != len(t):
            return False
        
        t_lookup = {}
        for i in range(0, len(t)):
            if t[i] in t_lookup:
                t_lookup[t[i]] += 1
            else:
                t_lookup[t[i]] = 1
        
        for char in s:
            if char in t_lookup:
                t_lookup[char] -= 1
                if t_lookup[char] <= 0:
                    del t_lookup[char]
            else:
                return False
        
        if len(t_lookup.keys()) == 0:
            return True

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))