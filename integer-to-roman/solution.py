class Solution:
    def intToRoman(self, num: int) -> str:
        """
        converts an integer into roman

        Args:
          num: the integer value to be converted to roman
        Returns:
          The roman representation of num
        """
        symbols_list = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500], #i
            ["CM", 900],
            ["M", 1000]
        ]

        i = len(symbols_list)-1
        roman = ""
        while num > 0:
            current_divider = symbols_list[i][1]
            current_symbol = symbols_list[i][0]
            
            result = num // current_divider
            if result > 0:
                temp = ""
                for _ in range(0, result):
                    temp += current_symbol
                roman += temp
                num %= current_divider
            i -= 1
        return roman

s = Solution()
print(s.intToRoman(1))
print(s.intToRoman(58))
print(s.intToRoman(1994))
print(s.intToRoman(128930))
