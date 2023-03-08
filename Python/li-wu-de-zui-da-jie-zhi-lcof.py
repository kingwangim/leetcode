# 剑指 Offer 47. 礼物的最大价值
# li-wu-de-zui-da-jie-zhi-lcof

class Solution:
    def maxValue(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i > 0:
                    f[i][j] = max(f[i][j], f[i - 1][j])
                if j > 0:
                    f[i][j] = max(f[i][j], f[i][j - 1])
                f[i][j] += grid[i][j]
        
        return f[m - 1][n - 1]
        
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().maxValue(grid))    