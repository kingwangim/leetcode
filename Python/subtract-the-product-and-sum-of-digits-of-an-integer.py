class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_list = []
        n_mul = 1
        for i in str(n):
            n_list.append(int(i))
            n_mul *= int(i)
        n_sum = sum(n_list)
        return n_mul-n_sum