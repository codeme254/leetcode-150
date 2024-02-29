class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        checks whether the characters in s can be replaced to get the
        characters in t (isomorphic strings)

        Args:
          s: first input string
          t: string to check against
        
        Returns:
          true if characters in s can be mapped to get the characters
          in t and false otherwise
        """
        if s == t:
            return True
        lookup = {}
        t_taken_chars = {}
        i=0
        j=0

        while i < len(s) and j < len(t):
            if s[i] in lookup:
                lookup_val = lookup[s[i]]
                if lookup_val != t[j]:
                    return False
            elif t[j] in t_taken_chars:
                return False
            else:
                lookup[s[i]] = t[j]
                t_taken_chars[t[j]] = True
            i += 1
            j += 1
        return True

s = Solution()
print(s.isIsomorphic("foo", "foo"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("add", "egg"))
print(s.isIsomorphic("title", "paper"))
print(s.isIsomorphic("badc", "baba"))