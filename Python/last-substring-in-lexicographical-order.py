import pdb

# # 一种骚操作
# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         res = ""
#         for i in range(len(s)):
#             res = max(res, s[i:])
#         return res

# 双指针
# 原题目转换成字典排序的最大子串即可
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                i += k + 1
                k = 0
                if i >= j:
                    j = i + 1
            else:
                j += k + 1
                k = 0
        return s[i:]

s = "leetcode"
print(Solution().lastSubstring(s))