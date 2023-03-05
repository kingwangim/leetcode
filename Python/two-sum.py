# 1. 两数之和
# two-sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, j in enumerate(nums):
            if target-j in nums[i+1:]: return [i, nums[i+1:].index(target-j)+i+1]

nums = [3,2,4]
target = 6
print(Solution().twoSum(nums, target))