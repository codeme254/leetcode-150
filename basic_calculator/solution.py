# solution from Timoth H Chang
class Solution:
    def calculate(self, s: str) -> int:
        """
        Evaluates a valid mathematical expression that is in string
        format and returns the integer result

        Args:
          s: input string that is a valid mathematical expression
        
        Returns:
          An integer value after the evaluation of mathematical expression s
        """
        output, cur, sign, stack = 0, 0, 1, []

        for c in s:
            if c.isdigit():
                cur = cur = cur * 10 + int(c)
            elif c in "+-":
                output += (cur * sign)
                cur = 0
                if c == "-":
                    sign = -1
                else:
                    sign = 1
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif c == ")":
                output += (cur * sign)
                output *= stack.pop()
                output += stack.pop()
                cur = 0
        return output + (cur * sign)

s = Solution()
print(s.calculate("222-111 + 2"))
print(s.calculate("1 + 1"))
print(s.calculate(" 2-1 + -2 "))
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))