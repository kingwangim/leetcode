import pdb
class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        res = []    
        m = len(l)
        for i in range(m):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            minus = temp[1] - temp[0]
            for j in range(len(temp)-1):
                sign = 0
                if minus != (temp[j+1] - temp[j]):
                    sign = 1
                    res.append(False)
                    break
            if sign == 0: res.append(True)

        return res

nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
print(Solution().checkArithmeticSubarrays(nums, l, r))