import pdb


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list[int], experience: list[int]) -> int:
        ans = 0
        # energy
        if sum(energy) >= initialEnergy: ans += sum(energy)-initialEnergy+1
        # experince
        for i in range(0, len(experience)):
            if experience[i] >= initialExperience:
                ans += experience[i] - initialExperience + 1
                initialExperience += experience[i] + \
                    experience[i] - initialExperience + 1
            else:
                initialExperience += experience[i]
        if ans > 0: return ans
        else: return 0


initialEnergy = 3
initialExperience = 2
energy = [1]
experience = [2]

print(Solution().minNumberOfHours(initialEnergy,
      initialExperience, energy, experience))
