class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for num in nums:
            if num < 0:
                if abs(num) in nums: return abs(num)
            else:
                return -1
        return -1