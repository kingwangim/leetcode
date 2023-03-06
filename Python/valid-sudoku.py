# 36. 有效的数独
# valid-sudoku

from collections import Counter
import pdb

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 判断 Row
        for i in range(9):
            j, temp = 0, []
            while j <9 :
                if len([index for (index, value) in enumerate(board[i]) if value == board[i][j]])>1 and board[i][j] != ".": return False
                j += 1
        # 判断 Col
        for i in range(9):
            j, temp = 0, []
            while j<9 :
                if board[j][i] in temp and board[j][i] != ".":
                    return False
                temp.append(board[j][i])
                j += 1
        # 判断3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = []
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] in temp and board[i+x][j+y]!=".": return False
                        temp.append(board[i+x][j+y])
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))