# 1625. 执行操作后字典序最小的字符串
# lexicographically-smallest-string-after-applying-operations

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # 枚举法
        # 累加操作数字最多累加 10 次还原
        # 轮转最多轮转 n 次还原
        ans = s
        n = len(s)
        s = list(s)
        for _ in range(n):
            s = s[-b:] + s[:-b]
            for j in range(10):
                for k in range(1, n, 2):
                    s[k] = str((int(s[k]) + a) % 10)
                if b & 1:
                    for p in range(10):
                        for k in range(0, n, 2):
                            s[k] = str((int(s[k]) + a) % 10)
                        t = ''.join(s)
                        if ans > t:
                            ans = t
                else:
                    t = ''.join(s)
                    if ans > t:
                        ans = t
        return ans

s = "5525"
a = 9
b = 2
print(Solution().findLexSmallestString(s, a, b))
