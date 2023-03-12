from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        sdic = Counter(s)
        for i, j in enumerate(s):
            if sdic[j] == 1: return i
        return -1
        

s = "leetcode"
print(Solution().firstUniqChar(s))