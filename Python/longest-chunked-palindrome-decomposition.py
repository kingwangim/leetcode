class Solution:
    def longestDecomposition(self, text: str) -> int:
        n, ans = len(text), 0
        prefix, suffix = [], []
        for i in range(n // 2):
            prefix.append(text[i])
            suffix.append(text[-(i+1)])
            if prefix == suffix[::-1]:
                ans += 2
                prefix = []
                suffix = []
        return ans+1 if n%2 or len(prefix) else ans

text = "ghiabcdefhelloadamhelloabcdefghi"
print(Solution().longestDecomposition(text))