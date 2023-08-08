class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # 动态规划法
        f_max = f_min = ans = 0
        for n in nums:
            f_max = max(f_max, 0) + n
            f_min = min(f_min, 0) + n
            ans = max(ans, f_max, -f_min)
        return ans

