class Solution:
    def squareDigits(self, n: int) -> int:
        """
        finds the sum of the square of digits in a number

        Args:
          n: input number
        
        Returns:
          the sum of square of digits in n
        """
        if n < 10:
            return n*n
        
        total = 0
        while n >= 10:
            left_most = n % 10
            total += pow(left_most, 2)
            n //= 10
        total += pow(n, 2)
        return total

    def isHappy(self, n: int) -> bool:
        """
        determines if a number is a happy number

        Args:
          n: input number
        
        Returns:
          true if n is a happy number and false otherwise
        """
        past_results = {}
        should_continue = True
        while should_continue:
            n = self.squareDigits(n)
            if n in past_results:
                print(past_results)
                return False
            if n == 1:
                return True
            past_results[n] = True

s = Solution()
print(s.squareDigits(5))
print(s.squareDigits(25))
print(s.squareDigits(255))
print(s.squareDigits(100))
print(s.isHappy(19))
print(s.isHappy(10))
print(s.isHappy(2))