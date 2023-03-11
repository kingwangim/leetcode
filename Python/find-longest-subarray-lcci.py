# 面试题 17.05.  字母与数字
# find-longest-subarray-lcci

class Solution:
    def findLongestSubarray(self, array: list[str]) -> list[str]:
        # res = [0, 0] 
        # num = char = 0
        # for i,j in enumerate(array):

        #     for k, w in enumerate(array[i:]):
        #         if w.isdigit():
        #             num += 1
        #         else:
        #             char += 1
        #         if num == char and res[1]-res[0] < (k-i): res=[i, k+1]
        # if res == [0, 0]: return []
        # else: return array[res[0]: res[1]]    

        indices = {0: -1}
        sum = 0
        maxLength = 0
        startIndex = -1
        for i, s in enumerate(array):
            if '0' <= s[0] <= '9':
                sum += 1
            else:
                sum -= 1
            if sum in indices:
                firstIndex = indices[sum]
                if i - firstIndex > maxLength:
                    maxLength = i - firstIndex
                    startIndex = firstIndex + 1
            else:
                indices[sum] = i
        if maxLength == 0:
            return []
        return array[startIndex: startIndex + maxLength]

# array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
array = ["A","A"]
print(Solution().findLongestSubarray(array))