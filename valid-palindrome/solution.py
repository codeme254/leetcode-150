class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks whether a string is palindrome

        Args:
          s: input string
        
        Returns:
          True if string s is palindrome, False otherwise
        """
        if len(s) == 1:
            return True
        temp_str = ""
        for char in s:
            temp_str += char.lower() if char.isalpha() or char.isnumeric() else ""
        
        if temp_str == "":
            return True
        
        i = 0
        j = len(temp_str)-1

        while i <= j:
            if temp_str[i] != temp_str[j]:
                return False
            i += 1
            j -= 1
        return True

s = Solution()
print(s.isPalindrome("# Race a car"))
print(s.isPalindrome("P"))
# print(s.isPalindrome("Eye"))
# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome(" "))