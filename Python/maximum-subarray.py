# 53. 最大子数组和
# maximum-subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # DP
        n = len(nums)
        if n == 0:
            return 0
        temp = 0
        res = nums[0]
        for i in range(n):
            temp = max(nums[i], temp + nums[i])
            res = max(res, temp)
        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))