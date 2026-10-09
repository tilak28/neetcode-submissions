class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0        #matrix top row
        bot = rows - 1 #matrix last row

        while top <= bot:
            mid_row = (top + bot) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1

            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break
        
        # the element might be too small or too large
        # so we cannot find it in either of the rows 
        if not (top <= bot):
            return False

        mid_row = (top + bot) // 2

        i = 0
        j = cols - 1

        while i <= j:
            mid = (i + j) // 2

            if target > matrix[mid_row][mid]:
                i = mid + 1
            elif target < matrix[mid_row][mid]:
                j = mid - 1
            else:
                return True
        return False

