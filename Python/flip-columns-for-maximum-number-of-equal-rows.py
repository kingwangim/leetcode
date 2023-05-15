from collections import Counter
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = Counter()
        for i in range(m):
            value = 0
            for j in range(n):
                value = value * 10 + (matrix[i][j] ^ matrix[i][0])
            count[value] += 1
        return max(count.values())
matrix = [[0,1],[1,1]]
print(Solution().maxEqualRowsAfterFlips(matrix))