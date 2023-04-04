import itertools
import functools

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):  # 无法合并成一堆
            return -1
        s = list(itertools.accumulate(stones, initial=0))  # 前缀和
        @functools.cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i == j:  # 只有一堆石头，无需合并
                return 0
            res = min(dfs(i, m) + dfs(m + 1, j) for m in range(i, j, k - 1))
            if (j - i) % (k - 1) == 0:  # 可以合并成一堆
                res += s[j + 1] - s[i]
            return res
        return dfs(0, n - 1)

stones = [3,2,4,1]
k = 2