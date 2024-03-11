class Solution:
    def isValid(self, s: str) -> bool:
        """
        determines if an input string bracket is valid

        Args:
          s: input string
        
        Returns:
          True if s is valid or false otherwise
        
        Description:
          A valid bracket string satisfies the following conditions
          Open brackets must be closed by the same type of brackets.  
          Open brackets must be closed in the correct order.  
          Every close bracket has a corresponding open bracket of the same type.  
        """
        stack = []
        openings = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        closings = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for i in range(0, len(s)):
            if s[i] in openings:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                recent = stack.pop()
                if closings.get(s[i]) != recent:
                    return False
        return len(stack) == 0

s = Solution()
print(s.isValid("(){}[]"))
print(s.isValid("()"))
print(s.isValid("(]"))
print(s.isValid("([{}])"))
print(s.isValid("]"))
print(s.isValid("]]]]]"))
print(s.isValid("[[[["))