class Solution:
    def isValid(self, s: str) -> bool:
        temp = "abc"
        if temp not in s:
            return False
        while len(s) != 0:
            if temp in s:
                s = s[:s.index(temp)]+s[s.index(temp)+len(temp):]
            else:
                return False
        return True