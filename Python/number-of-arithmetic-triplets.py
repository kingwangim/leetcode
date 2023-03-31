class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        res = []
        for i in range(len(nums)):
            if nums[i]+diff in nums and nums[i]+diff*2 in nums:
                res.append([i, nums.index(nums[i]+diff),
                           nums.index(nums[i]+diff*2)])
        return len(res)


nums = [0, 1, 4, 6, 7, 10]
diff = 3
print(Solution().arithmeticTriplets(nums, diff))
