from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        invalid_zeros = {}
        row = 0

        while row < len(matrix):
            column = 0
            while column < len(matrix[0]):
                # print(matrix[row][column])
                if matrix[row][column] == 0:
                    row_column_intersection = str(row)+"_"+str(column)
                    if row_column_intersection in invalid_zeros:
                        column += 1
                    else:
                        top_fill = row - 1
                        while top_fill >= 0:
                            if matrix[top_fill][column] == 0:
                                top_fill -= 1
                                continue
                            matrix[top_fill][column] = 0
                            invalid_zeros[str(top_fill)+"_"+str(column)] = True
                            top_fill -= 1
                        
                        bottom_fill = row + 1
                        while bottom_fill < len(matrix):
                            if matrix[bottom_fill][column] == 0:
                                bottom_fill += 1
                                continue
                            matrix[bottom_fill][column] = 0
                            invalid_zeros[str(bottom_fill)+"_"+str(column)] = True
                            bottom_fill += 1
                        
                        left_fill = column-1
                        while left_fill >= 0:
                            if matrix[row][left_fill] == 0:
                                left_fill -= 1
                                continue
                            matrix[row][left_fill] = 0
                            invalid_zeros[str(row)+"_"+str(left_fill)] = True
                            left_fill -= 1
                        
                        right_fill = column+1
                        while right_fill < len(matrix[0]):
                            if matrix[row][right_fill] == 0:
                                right_fill += 1
                                continue
                            matrix[row][right_fill] = 0
                            invalid_zeros[str(row)+"_"+str(right_fill)] = True
                            right_fill += 1
                        column += 1
                else:
                    column += 1
            row += 1
        print(matrix)
        print(sorted(invalid_zeros.keys()))

s = Solution()
# s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
# s.setZeroes([[0],[1]])
# s.setZeroes([[1],[0]])
# s.setZeroes([[9,8,5,1,8,0,7,3,4,1,2,0],[1,4,3,3,8,1,6,9,3,5,7,3],[2,5,0,9,5,9,6,4,8,4,7,6],[4,5,2,0,8,4,3,1,0,6,4,8],[9,0,9,5,7,7,0,9,2,2,0,9],[2,7,6,2,1,3,0,7,0,2,7,0],[6,0,2,8,9,6,6,0,9,6,7,6],[3,8,8,7,0,8,9,4,7,5,6,0],[0,9,7,3,1,7,3,0,9,7,8,8],[6,7,1,5,3,8,3,8,6,1,7,9],[2,6,3,9,1,2,2,4,1,9,7,4],[8,0,4,8,8,5,8,4,2,9,1,7]])
# s.setZeroes([[1,1,1],[1,0,1],[1,0,1]])