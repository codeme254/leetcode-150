from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotated = []
        i = 0

        while i < len(matrix[0]):
            current = len(matrix)-1
            current_arr = []
            while current >= 0:
                current_arr.append(matrix[current][i])
                current -= 1
            i += 1
            rotated.append(current_arr)
        
        for i in range(0, len(matrix)):
            matrix[i] = rotated[i]
        rotated = []
        print(matrix)

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])