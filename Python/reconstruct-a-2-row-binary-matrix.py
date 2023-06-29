import pdb
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: list[int]) -> list[list[int]]:
        if upper + lower != sum(colsum): return []
        sum_2 = len([index for (index, value) in enumerate(colsum) if value == 2])
        if upper < sum_2 or lower < sum_2: return []
        res_upper, res_lower = [], []
        upper_sum = 0
        colsum_temp = colsum[:]
        colsum_temp.sort(reverse=True)
        for i in colsum_temp:
            if i == 2:
                upper -= 1
            if i == 1 and upper >= 1:
                upper -= 1
                upper_sum += 1
        for i in range(len(colsum)):
            if colsum[i] == 2:
                res_upper.append(1)
                res_lower.append(1)
            if colsum[i] == 1 and upper_sum >= 1:
                upper_sum -= 1
                res_upper.append(1)
                res_lower.append(0)
            elif colsum[i] == 1 and upper_sum < 1:
                res_upper.append(0)
                res_lower.append(1)
            if colsum[i] == 0:
                res_upper.append(0)
                res_lower.append(0)
        return [res_upper, res_lower]            
        
upper = 9
lower = 2
colsum = [0,1,2,0,0,0,0,0,2,1,2,1,2]
print(Solution().reconstructMatrix(upper, lower, colsum))