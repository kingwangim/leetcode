class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        res = []
        while(len(nums) != 0 ):
            maxnum = max(nums)
            minnum = min(nums)
            nums.remove(maxnum)
            nums.remove(minnum)
            avg = (maxnum + minnum) / 2
            if avg not in res: res.append(avg)
        return len(res)

nums = [1, 100]
print(Solution().distinctAverages(nums))