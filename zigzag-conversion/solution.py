class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Returns the zigzag conversion of string s
        Args:
          s: the string to be converted to zigzag
          numRows: the number of rows of the zigzag
        Returns:
          the zigzag equivalent of string s
        """

        if len(s) == 1 or numRows == 1:
            return s
        
        rows = []
        for _ in range(0, numRows):
            rows.append("")
        
        i = 0
        direction = "up"
        k = 0
        while k < len(s):
            rows[i] += s[k]
            if direction == "up":
                if i + 1 >= numRows:
                    i -= 1
                    direction = "down"
                else:
                    i += 1
            elif direction == "down":
                if i-1 < 0:
                    i += 1
                    direction = "up"
                else:
                    i -= 1
            k += 1
        
        return "".join(rows)

s = Solution()
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("A", 1))
print(s.convert("A", 10))