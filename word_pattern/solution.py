class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        checks if a sentence follows a pattern in a given word

        Args:
          pattern: word with the pattern
          s: input sentence
        """
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        i = 0
        j = 0
        lookup = {}
        taken_words = {}
        while i < len(pattern) and j < len(s):
            if pattern[i] in lookup:
                value = lookup[pattern[i]]
                if value != s[j]:
                    return False
            elif pattern[i] not in lookup:
                if s[j] in taken_words:
                    return False
                lookup[pattern[i]] = s[j]
                taken_words[s[j]] = True
            i += 1
            j += 1
        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("aaaa", "dog cat cat dog"))