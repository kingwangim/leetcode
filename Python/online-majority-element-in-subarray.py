from collections import Counter
import pdb

# # 超时
# class MajorityChecker:

#     def __init__(self, arr: list[int]):
#         self.MajorityChecker = arr

#     def query(self, left: int, right: int, threshold: int) -> int:
#         arr = self.MajorityChecker
#         temp = arr[left: right+1]
#         tempsort = Counter(temp)
#         pdb.set_trace()
#         def find_keys_with_given_count(counter, count):
#             for key, value in counter.items():
#                 if value >= count:
#                     pdb.set_trace()
#                     return key
#             return -1   
#         return find_keys_with_given_count(tempsort, threshold)     

#  随机化 + 二分查找
class MajorityChecker:
    k = 20

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.loc = defaultdict(list)

        for i, val in enumerate(arr):
            self.loc[val].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        arr_ = self.arr
        loc_ = self.loc
        
        length = right - left + 1
        for i in range(MajorityChecker.k):
            x = arr_[randint(left, right)]
            pos = loc_[x]
            occ = bisect_right(pos, right) - bisect_left(pos, left)
            if occ >= threshold:
                return x
            elif occ * 2 >= length:
                return -1

        return -1

# Input
arr = [2,1,2,1,2,2,2,2,2,1,2,2,1,1,1,1,2,1,1,1,1,2]
query = [2,8,5]
left, right, threshold = query[0], query[1], query[2]

# Your MajorityChecker object will be instantiated and called as such:
obj = MajorityChecker(arr)
param_1 = obj.query(left,right,threshold)
print(param_1)