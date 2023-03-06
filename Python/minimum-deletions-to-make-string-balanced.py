# 1653. 使字符串平衡的最少删除次数
# minimum-deletions-to-make-string-balanced

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        # dp
        a = b = 0
        for c in s:
            if c == "a":
                b = min(a, b + 1)
            else:
                a = a + 1
        return b

s = "aababbab"
print(Solution().minimumDeletions(s))