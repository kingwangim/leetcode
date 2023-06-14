import pdb
class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[k]!=nums[i]:
                        ans += 1
        return ans
    
nums = [1,1,1,1,1]
print(Solution().unequalTriplets(nums))
        