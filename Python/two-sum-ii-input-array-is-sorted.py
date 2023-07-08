class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 双指针
        # 二分查找
        n = len(numbers)
        l, r = 0, n-1
        while( l < r and numbers[l] + numbers[r] != target):
            if numbers[l] + numbers[r] < target :
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]