from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNotedic = Counter(ransomNote)
        magazinedic = Counter(magazine)
        for item in ransomNotedic:
            if item in magazinedic:
                if ransomNotedic[item] > magazinedic[item]:
                    return False
            else:
                return False
        return True 


ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))    