class Solution:
    def reverseWords(self, s: str) -> str:
        """
        reverses words in a string

        Args:
          s: input string
        
        Returns:
          a string with words in reverse order of appearance in s
        """

        s_arr = s.strip().split()
        
        reversed_str = ""
        i = len(s_arr)-1

        while i >= 0:
            if s_arr[i] == " " and reversed_str[len(reversed_str)-1] == " ":
                i -= 1
            else:
                reversed_str += f"{s_arr[i]} "
                i -= 1
        return reversed_str.strip()

s = Solution()
print(s.reverseWords("Hello"))