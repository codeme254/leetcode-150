from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        return all the elements of a matrix in spiral order

        Args:
          matrix: input 2-d array / matrix
        
        Returns:
          all the elements of the matrix in spiral order
        """

        result = []

        x = 0
        j = 0

        y = 0
        k = len(matrix[0])-1

        w = len(matrix)-1
        m = len(matrix[0])-1

        z = len(matrix)-1
        n = 0

        while True:
            temp_j = j
            while j < k:
                result.append(matrix[x][j])
                j += 1
            
            temp_y = y
            while y < w:
                result.append(matrix[y][k])
                y += 1
            
            temp_m = m
            while m > n:
                result.append(matrix[w][m])
                m -= 1
            
            temp_z = z
            while z > x:
                result.append(matrix[z][n])
                z -= 1
            
            x += 1
            j = temp_j + 1
            k -= 1
            y = temp_y + 1
            w -= 1
            m = temp_m - 1
            z = temp_z - 1
            n += 1

            
            if y > w or x > z:
                break
        
        return result

s = Solution()
print(s.spiralOrder([[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5],[6,7,8,9,0]]))
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))