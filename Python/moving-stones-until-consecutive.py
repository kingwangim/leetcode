class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        nums = [a, b, c]
        nums.sort()
        a, b, c = nums[0], nums[1], nums[2]
        res, minm, maxm = [], 0, 0

        # 基本情况
        if c-b > 1:
            minm += 1
            maxm += c-b-1
        if b-a > 1:
            minm += 1
            maxm += b-a-1
        # bc间距更小的情况
        if c-b-1 == 1 or b-a-1 == 1:
            minm = 1

        res.append(minm)
        res.append(maxm)

        return res
