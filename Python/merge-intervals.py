class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals:
            interval_l, interval_r = interval[0], interval[1]
            res_l, res_r = res[-1][0], res[-1][1]
            if interval_l <= res_r and interval_l >= res_l:
                if interval_r >= res_r:
                    res[-1][1] = interval_r 
            else:
                res.append(interval)
        return res