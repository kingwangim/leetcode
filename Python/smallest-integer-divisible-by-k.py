class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 ==0:
            return -1
        i, temp, ans = 1, 1, 1
        while(i % k != 0):
            temp *= 10
            i += temp
            ans += 1
        return ans


k = 3
print(Solution().smallestRepunitDivByK(k))
