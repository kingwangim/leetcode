class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 滑窗问题 取窗口内w个数的最小值
        if k*"B" in blocks: return 0
        n = len(blocks)
        res = []
        for i in range(0, n-k+1):
            res.append(len([index for (index, value) in enumerate(blocks[i:i+k]) if value == "W"]))
        return min(res)
blocks = "WBWW"
k = 2
print(Solution().minimumRecolors(blocks, k))