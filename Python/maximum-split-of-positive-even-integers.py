import pdb
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        res, temp = [], 2
        if finalSum % 2 != 0:
            return res
        while finalSum != 0:
            if finalSum >= temp:
                res.append(temp)
                finalSum -= temp
                temp += 2
            else:
                res[-1] += finalSum
                finalSum = 0
        return res

finalSum = 12
print(Solution().maximumEvenSplit(finalSum))