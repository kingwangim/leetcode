class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(n, 0, -1):
            if (1+x)*x/2 == (n+x)*(n-x+1)/2:
                return x 
        return -1