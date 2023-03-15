import pdb
class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        g = [[0] * n for _ in range(n)]
        cnt = [0] * n
        for a, b in roads:
            g[a][b] = g[b][a] = 1
            cnt[a] += 1
            cnt[b] += 1
        return max(cnt[a] + cnt[b] - g[a][b] for a in range(n) for b in range(a + 1, n))
                
        
n = 2
roads = [[1,0]]
print(Solution().maximalNetworkRank(n, roads))