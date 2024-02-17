class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        finds the index of first occurence of string needle in string haystack

        Args:
          haystack: the string to search needle from
          needle: the string to find in haystack

        Returns:
          the first occurence of needle in stack or -1 if it is not present
        """
        if len(needle) > len(haystack):
            return -1
        occurence = 0
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                occurence = i
                j = i
                temp_str = ""
                while j < len(haystack) and len(temp_str) < len(needle):
                    temp_str += haystack[j]
                    j += 1
                if temp_str == needle:
                    return occurence
        return -1

s = Solution()
print(s.strStr("butsadsad", "sad"))
print(s.strStr("leetcode", "leeto"))
print(s.strStr("leetc", "leetcode"))
print(s.strStr("l", "l"))