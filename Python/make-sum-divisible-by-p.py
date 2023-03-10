from itertools import accumulate

class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        # 暴力法 超时
        # count = sum(nums)   
        # if count % p == 0: return 0
        # res = []
        # for i, num in enumerate(nums):
        #     ans = 0
        #     if (count-num)%p == 0: 
        #         ans +=1
        #         return ans
        #     else:
        #         # 子数组需要连续
        #         j = i+1
        #         while(j<=len(nums)):
        #             if (count - sum(nums[i: j]))%p == 0:
        #                 ans = len(nums[i: j])
        #                 if ans!=len(nums): res.append(ans) 
        #             j += 1
        # if len(res) > 0: return min(res)
        # else: return -1

        # 前缀和 + 哈希表
        s = list(accumulate(nums, initial=0))
        x = s[-1] % p
        
        ans = n = len(nums)
        last = {}
        for i, v in enumerate(s):
            last[v % p] = i
            j = last.get((v - x) % p, -n)  # 如果不存在，-n 可以保证 i-j >= n
            ans = min(ans, i - j)
        return ans if ans < n else -1

nums = [1000000000,1000000000,1000000000]
p = 3
print(Solution().minSubarray(nums, p))        