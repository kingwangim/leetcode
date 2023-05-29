class Solution:
    def averageValue(self, nums: list[int]) -> int:
        sums = times = 0
        for num in nums:
            if num % 3 == 0 and num % 2 == 0:
                sums += num
                times += 1
        if sums != 0:
            return int(sums/times)
        else:
            return 0

nums = [1,2,4,7,10]
print(Solution().averageValue(nums))
