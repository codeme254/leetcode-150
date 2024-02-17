from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        finds the longest common prefix from a list of strings
        Args:
          strs: a list of strings
        Returns:
          the longest common prefix or an empty string if it is not there
        """

        prefix = ""
        shortest_string = strs[0]
        for str in strs:
            if len(str) <= len(shortest_string):
                shortest_string = str
        i = 0
        while i < len(shortest_string):
            current = strs[0][i]
            for str in strs:
                if current != str[i]:
                    return prefix
            prefix += current
            i += 1
        return prefix

s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flowing"]))
print(s.longestCommonPrefix(["flower"]))
print(s.longestCommonPrefix(["flower", "guns", "roses"]))