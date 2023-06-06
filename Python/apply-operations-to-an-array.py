class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        res = []
        for num in nums:
            if num != 0:
                res.append(num)
        res.extend((len(nums)-len(res)) * [0])
        return res

nums = [0, 1]
print(Solution().applyOperations(nums))