# 350. 两个数组的交集 II
# intersection-of-two-arrays-ii

from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        
        # 哈希
        nums1 = Counter(nums1)
        res = []
        for i in nums2:
            if i in nums1 and nums1[i]:
                res.append(i)
                nums1[i] -= 1
        return res


nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1, nums2))   