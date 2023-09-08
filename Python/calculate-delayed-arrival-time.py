class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        resTime = arrivalTime + delayedTime
        return resTime % 24