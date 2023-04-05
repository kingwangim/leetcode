class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n = min(a, b)
        res = []
        for i in range(1, n+1):
            if a % i == 0 and b % i == 0:
                res.append(i)
            
        return len(set(res))
        # return res

a = 12
b = 6
print(Solution().commonFactors(a, b))