import pdb
from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(Counter(word).values())
        t = list(cnt)
        pdb.set_trace()
        # 字母均出现一次的情况
        if len(t) == 1 and t[0] == 1:
            return True  
        # 所有字母相同的情况
        if len(set(word)) == 1:
            return True
        # 字母出现多次的情况
        if len(t) == 2:
            t.sort()
            x, y = t[0], t[1]
            if x == 1 and cnt[x] == 1:
                return True
            if x+1 == y and cnt[y] == 1:
                return True
        return False 

word = "cbccca"
print(Solution().equalFrequency(word))