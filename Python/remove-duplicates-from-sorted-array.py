from collections import Counter
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        numssort = Counter(nums)
        for key, value in numssort.items():
            for v in range(value-1):
                nums.remove(key)
        return nums

nums = [1,1,2]
print(Solution().removeDuplicates(nums))