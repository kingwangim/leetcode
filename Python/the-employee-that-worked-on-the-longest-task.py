import pdb
class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        ans = logs[0][0]
        tempt = logs[0][1]
        for i in range(1, len(logs)):  
            t = logs[i][1] - logs[i-1][1]
            if t > tempt:
                ans = logs[i][0]
                tempt = t
            if t == tempt:
                ans = min(ans, logs[i][0])
                tempt = t
            # pdb.set_trace()
        return ans    


n = 145
logs = [[114,5],[115,7],[50,9],[105,11],[18,13],[47,16],[48,18],[39,19]]
print(Solution().hardestWorker(n, logs))