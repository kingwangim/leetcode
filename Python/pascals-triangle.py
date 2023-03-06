# 118. 杨辉三角
# pascals-triangle

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):   
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i-1][j]+res[i-1][j-1])
            res.append(row)
        return res

numRows = 5
print(Solution().generate(numRows))
