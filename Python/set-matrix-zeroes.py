import pdb
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp  = [it.copy() for it in matrix]
        for i in range(len(temp)):
            list0 = [index for (index, value) in enumerate(temp[i]) if value == 0]
            if len(list0) != 0:
                # 行
                matrix[i] = [0]*len(temp[i])    
                # 列
                for j in list0:
                    for k in range(len(temp)):
                        matrix[k][j] = 0
        print(matrix)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)