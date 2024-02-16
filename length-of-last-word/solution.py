class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        finds the length of the last word in a string

        Args:
            s: input string
        Returns:
            The length of the last word in s
        """
        s = s.strip()

        i = len(s)-1
        length = 0
        while s[i] != " " and i >= 0:
            length += 1
            i -= 1
        return length

s = Solution()
print(s.lengthOfLastWord("  fly me to  the moon   "))
print(s.lengthOfLastWord("Hello, World"))
print(s.lengthOfLastWord("luffy is still joyboy"))