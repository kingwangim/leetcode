import pdb
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        peoples, res = [], []
        for i in range(len(names)):
           peoples.append([heights[i], names[i]])
        peoples.sort(reverse=True)
        for people in peoples:
            res.append(people[1])
        return res
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(Solution().sortPeople(names,heights))