class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0

        dict_square = {}
        while i < 9:
            dict_row = {}
            j = 0
            
            while j < 9:
                value = board[i][j]
                
                if value != ".":
                    square = (i // 3, j // 3)
                    if square not in dict_square:
                        dict_square[square] = {}

                    if value in dict_square[square]:
                        return False

                    dict_square[square][value] = 1

                    if value in dict_row:
                        return False

                    dict_row[value] = 1
                
                j+= 1
            
            i+=1

        j = 0

        while j < 9:
            dict_col = {}
            i = 0

            while i < 9:
                value = board[i][j]

                if value != ".":
                    if value in dict_col:
                        return False

                    dict_col[value] = 1

                i+=1
            
            j+=1

        return True

        