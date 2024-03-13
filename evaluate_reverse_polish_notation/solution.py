from typing import List
from math import trunc
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        evaluates an expression that is in reverse polish notation.

        Args:
          tokens: a list of tokens
        
        Returns:
          an integer value after evaluating the notation
        """
        valid_operators = {
            '+': "plus",
            '-': "minus",
            '*': "multiplication",
            '/': "division"
        }

        operands = []

        for token in tokens:
            if token in valid_operators:
                first_operand = operands.pop()
                second_operand = operands.pop()
                current_eval = 0
                if token == "*":
                    current_eval = first_operand * second_operand
                elif token == "+":
                    current_eval = first_operand + second_operand
                elif token == "-":
                    current_eval = second_operand - first_operand
                elif token == "/":
                    if first_operand != 0 and second_operand != 0:
                        current_eval = trunc(second_operand/first_operand)
                operands.append(current_eval)
            else:
                operands.append(int(token))
        return operands[0]

s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(s.evalRPN(["10"]))
# print(s.evalRPN(["10", "+"]))
print(s.evalRPN(["10", "3", "+"]))
print(s.evalRPN(["4", "3", "-"]))