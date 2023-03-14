class Solution:
    def restoreresrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        i = j = 0  # 从左上角出发
        while i < m and j < n:
            rs, cs = rowSum[i], colSum[j]
            if rs < cs:
                res[i][j] = rs  # 去掉第 i 行
                colSum[j] -= rs
                i += 1  # 往下走
            else:
                res[i][j] = cs  # 去掉第 j 列
                rowSum[i] -= cs
                j += 1  # 往右走
        return res

rowSum = [3,8]
colSum = [4,7]
print(Solution().restoreresrix(rowSum, colSum))