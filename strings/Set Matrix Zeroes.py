class Solution:
    def rowZero(self, row_number, matrix):
        for col in range(len(matrix[0])):
            matrix[row_number][col] = 0
        
    def colZero(self, col_number, matrix):
        for row in range(len(matrix)):
            matrix[row][col_number] = 0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    lst.append([row, col])
        
        for record in lst:
            self.rowZero(record[0], matrix)
            self.colZero(record[1], matrix)

        
