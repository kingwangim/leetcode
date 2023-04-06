class Solution:
    def baseNeg2(self, n: int) -> str:
        res = ''
        while n:
            n, k = -(n // 2), n % 2
            res += str(k)
        
        return res[::-1] if res else '0'


n = 4
print(Solution().baseNeg2(n))