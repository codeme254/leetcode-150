from typing import List
class Solution:
    def isAnagramOf(self, str1: str, str2: str):
        """
        Checks if the characters of str2 can be rearranged to form str1
        i.e checks if str2 is a valid anagram of str1

        Args:
          str1: string to check agains
          str2: supposed string
        
        Returns:
          true if str2 is a valid anagram of str1
        """
        if len(str1) != len(str2):
            return False
        
        str2_lookup = {}
        for char in str2:
            if char in str2_lookup:
                str2_lookup[char] += 1
            else:
                str2_lookup[char] = 1

        for char in str1:
            if char not in str2_lookup:
                return False
            str2_lookup[char] -= 1
            if str2_lookup[char] == 0:
                del str2_lookup[char]

        if len(str2_lookup.keys()) == 0:
            return True
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        groups anagrams from a list of strings together

        Args:
          strs: list of strings
        
        Returns:
          a list of lists of strings where each nested list contains
          strings that are anagrams of one another
        """
        if len(strs) == 1:
            return [[strs[0]]]
        
        result = []
        found_anagrams = {}
        for i in range(0, len(strs)):
            current_str = strs[i]
            if current_str in found_anagrams:
                continue
            current_group = []
            current_group.append(current_str)
            for j in range(i+1, len(strs)):
                if self.isAnagramOf(current_str, strs[j]):
                    current_group.append(strs[j])
                    found_anagrams[strs[j]] = True
            result.append(current_group)
        return result

s = Solution()
print(s.isAnagramOf("happy", "happy"))
print(s.isAnagramOf("tea", "ate"))
print(s.isAnagramOf("tea", "eat"))
print(s.isAnagramOf("tea", "bat"))
print(s.isAnagramOf("", " "))
print(s.isAnagramOf("b", " "))

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))