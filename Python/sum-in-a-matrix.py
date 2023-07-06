class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = 0
        while (len(nums[0]) > 0):
            temp = []
            for num in nums:
                maxval = max(num)
                temp.append(maxval)
                del num[num.index(maxval)]
            ans += max(temp)
        return ans
