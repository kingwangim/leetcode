class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = []
        for str in strs:
            if str.isdigit():
                res.append(int(str))
            else:
                res.append(len(str))
        return max(res)