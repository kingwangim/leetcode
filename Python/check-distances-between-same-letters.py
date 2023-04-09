import pdb
class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        def num(chr):
            return ord(chr)-97
        for i in set(s):
            chr_index = [index for (index, value) in enumerate(s) if value == i]
            # pdb.set_trace()
            if len(chr_index) < 2: return False
            chr_distance = chr_index[1]-chr_index[0]-1
            # pdb.set_trace()
            if distance[num(i)]!=chr_distance: return False
        return True

s = "aa"
distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(Solution().checkDistances(s, distance))