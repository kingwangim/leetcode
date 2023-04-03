class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        for i in range(len(arr)-1,0 ,-1):
            if arr[i-1] > arr[i]:
                for j in range(len(arr)-1,i-1,-1):
                    if arr[j] < arr[i-1] and arr[j] != arr[j-1]:
                        arr[i-1],arr[j] = arr[j], arr[i-1]
                        return arr
        return arr

arr = [3,2,1]
print(Solution().prevPermOpt1(arr))
