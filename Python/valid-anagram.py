from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = Counter(s)
        tdic = Counter(t)
        if len(sdic) != len(tdic): return False
        for i in s:
            if i in tdic:
                if sdic[i] != tdic[i]: return False
            else:
                return False
        return True
s = "a"
t = "ab"
print(Solution().isAnagram(s, t))