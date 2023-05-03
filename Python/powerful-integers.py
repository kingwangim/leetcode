import pdb
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        res = []
        for i in range(21):
            if pow(x, i) > bound:
                break
            for j in range(21):
                ans = x**i+y**j
                if ans > bound:
                    break
                if ans <= bound:
                    if ans not in res: res.append(ans)
        res.sort()
        return res

x = 3
y = 5
bound = 15
print(Solution().powerfulIntegers(x, y, bound))