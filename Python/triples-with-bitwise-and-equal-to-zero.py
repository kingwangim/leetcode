from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        # 枚举法
        cnt = Counter((x&y) for x in nums for y in nums)
        ans = 0
        for i in nums:
            for j, k in cnt.items():
                if (i&j) == 0:
                    ans += k
        return ans