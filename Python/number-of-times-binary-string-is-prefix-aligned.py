import pdb
class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        ans = mx = 0
        for i, x in enumerate(flips, 1): 
            mx = max(mx, x)
            ans += mx == i
        return ans
    
flips = [3,2,4,1,5]
print(Solution().numTimesAllBlue(flips))