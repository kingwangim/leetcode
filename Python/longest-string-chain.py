import pdb
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # 反向实现，从最长的字符串中删除元素进行计算
        words.sort(key=len, reverse=True)
        ans, mp = 0, defaultdict(lambda: 1)
        for word in words:
            for i in range(len(word)):
                temp = word[:i] + word[i+1:]   # 删除一个元素的字符串
                if temp in words:
                    mp[temp] = max(mp[temp], mp[word]+1)
                    ans = max(ans, mp[temp])
        if ans == 0: return 1
        else: return ans


words = ["a","b","ba","bca","bda","bdca"]
print(Solution().longestStrChain(words))