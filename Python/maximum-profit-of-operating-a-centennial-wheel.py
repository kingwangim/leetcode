# 1599. 经营摩天轮的最大利润

class Solution:
    def minOperationsMaxProfit(self, customers: list[int], boardingCost: int, runningCost: int) -> int:
        ans = []
        nowcustomers = profits = times = 0
        # 模拟，当前游客数量不为 0 或仍有新游客到达时
        while nowcustomers != 0 or times < len(customers):
            # 新抵达游客
            if times < len(customers):
                nowcustomers += customers[times]
                times += 1
            # 计算当前利润
            if nowcustomers >= 4:
                profits += 4 * boardingCost - runningCost
                nowcustomers -= 4
            else:
                profits += nowcustomers * boardingCost - runningCost
                nowcustomers = 0
            ans.append(profits)
        if max(ans) <= 0: return -1
        return ans.index(max(ans)) + 1
        
    
customers = [2]
boardingCost = 2
runningCost = 4
print(Solution().minOperationsMaxProfit(customers, boardingCost, runningCost))