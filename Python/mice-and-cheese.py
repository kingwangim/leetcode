import pdb
class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        scores, diff, score = 0, [], 0
        scores = sum(reward2)
        for i in range(len(reward1)):
            diff.append(reward1[i]-reward2[i])
        diff.sort(reverse=True)
        for i in range(k):
            scores += diff[i]
        return scores
            


reward1 = [1,1,3,4]
reward2 = [4,4,1,1]
k = 2
print(Solution().miceAndCheese(reward1, reward2, k))    