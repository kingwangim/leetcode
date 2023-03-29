# 数学方法
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return int((n + 4) * (n + 3) * (n + 2) * (n + 1)/24)
    
if __name__ == "__main__":
    n = 1
    print(Solution().countVowelStrings(n))