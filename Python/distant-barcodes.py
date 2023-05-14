from collections import Counter
import pdb
class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        l = len(barcodes)
        nums, res = [], [0] * l
        for i, j in Counter(barcodes).most_common():
            nums += [i] * j
        res[::2] = nums[:(l+1)//2]
        res[1::2] = nums[(l+1)//2:]
        return res

barcodes = [1,1,1,1,2,2,3,3]
print(Solution().rearrangeBarcodes(barcodes))