# 217. 存在重复元素
# contains-duplicate

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) > len(set(nums)): return True
        return False

nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))