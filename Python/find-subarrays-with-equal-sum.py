class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        res = []
        for i in range(len(nums)-1):
            temp = nums[i] + nums[i+1]
            if temp not in res:
                res.append(temp)
            else:
                return True
        return False