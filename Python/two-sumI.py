class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            x = target - nums[i]
            if x in nums[i+1:]:
                return [i, nums[i+1:].index(x)+i+1]