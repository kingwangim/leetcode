# 1637. 两点之间不包含任何点的最宽垂直区域
# widest-vertical-area-between-two-points-containing-no-points

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()
        res = []
        for i in range(1, len(points)):
            res.append(points[i][0]-points[i-1][0])
        return max(res) 

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(Solution().maxWidthOfVerticalArea(points))