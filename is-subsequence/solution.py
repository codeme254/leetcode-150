class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        checks whether a string is a subsequence of another

        Args:
          s: first string
          t: string to check against
        
        Returns:
          True if s is a subsequence of t, false otherwise
        """
        if s == "":
            return True
        if len(s) > len(t):
            return False
        if s == t:
            return True
        if len(s) == len(t) and s != t:
            return False
        
        i = 0
        j = 0

        while j < len(t):
            if s[i] == t[j]:
                i += 1
                if i > len(s)-1:
                    return True
            j += 1
        
        return False

s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))
print(s.isSubsequence("ahbgdc", "ahbgdc"))
print(s.isSubsequence("ahbgdk", "ahbgdc"))
print(s.isSubsequence("ahbgdk", "ahb"))