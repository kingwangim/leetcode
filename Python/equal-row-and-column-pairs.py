class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = grid[:]
        cols = []
        ans = 0
        for i in range(len(rows[0])):
            temp = []
            for j in range(len(rows)):
                temp.append(rows[j][i])
            cols.append(temp)
        for col in cols:
            ans += len([index for (index, value)
                       in enumerate(rows) if value == col])
        return ans
