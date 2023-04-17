import pdb
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # 月份转化为相对于年初的天数
        def MonthsToYears(dates):
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            month, day = int(dates.split("-")[0]), int(dates.split("-")[1])
            days = sum(months[:month-1])+day
            return days
        arriveAlice, leaveAlice = MonthsToYears(
            arriveAlice), MonthsToYears(leaveAlice)
        arriveBob, leaveBob = MonthsToYears(arriveBob), MonthsToYears(leaveBob)
        
        if arriveBob > leaveAlice or arriveAlice > leaveBob:
            return 0
        if arriveBob > arriveAlice:
            if leaveBob > leaveAlice:
                return leaveAlice-arriveBob+1
            else:
                return leaveBob-arriveBob+1
        else:
            if leaveAlice > leaveBob:
                return leaveBob-arriveAlice+1
            else:
                return leaveAlice-arriveAlice+1

arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))