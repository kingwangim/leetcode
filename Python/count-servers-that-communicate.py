class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        # 先按行遍历，找出一行中所有可以通信的情况
        for i in range(m):
            if sum(grid[i]) >= 2:
                ans += sum(grid[i])
            elif sum(grid[i]) == 1:
                j = grid[i].index(1)
                for k in range(m):
                    if k != i:
                        if grid[k][j] == 1:
                            ans += 1
                            break
        return ans
