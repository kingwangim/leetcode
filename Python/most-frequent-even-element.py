import pdb
from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        res = []
        nums = Counter(nums)
        nums = {key: value for key, value in nums.items() if key % 2 == 0}
        if len(nums) == 0: return -1
        else: return min({key: value for key, value in nums.items() if value == max(nums.values())}.keys())    

nums =  [4,4,4,9,2,4]
print(Solution().mostFrequentEven(nums))