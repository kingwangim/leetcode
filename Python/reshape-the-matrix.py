# 566. 重塑矩阵
# reshape-the-matrix

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        res = []
        items = []
        if len(mat)*len(mat[0]) != r*c: return mat
        for i in mat:
            for j in i:
                items.append(j)
        for i in range(0, len(items), c):
            res.append(items[i:i+c])
        return res

mat = [[1, 2], [3, 4]]
r = 2
c = 2
print(Solution().matrixReshape(mat, r, c))
