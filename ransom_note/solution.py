class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Checks if a ransom note can be constructed by using letters from
        a magazine

        Args:
          ransomNote: ransom note string
          magazine: magazine string
        
        Returns:
          true if the ransom note can be constructed by using letters from the
          magazine and false otherwise
        """
        if len(ransomNote) > len(magazine):
            return False
        magazine_lookup = {}

        for i in range(0, len(magazine)):
            if magazine[i] in magazine_lookup:
                magazine_lookup[magazine[i]].append(i)
            else:
                magazine_lookup[magazine[i]] = [i]
        
        for i in range(0, len(ransomNote)):
            if ransomNote[i] in magazine_lookup:
                if len(magazine_lookup[ransomNote[i]]) == 1:
                    del magazine_lookup[ransomNote[i]]
                else:
                    magazine_lookup[ransomNote[i]].pop()
            else:
                return False
        return True

s = Solution()
print(s.canConstruct("hit", "hhit"))
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("aaaaaa", "aab"))