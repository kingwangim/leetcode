class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1time1, event1time2 = event1[0].replace(":", ""), event1[1].replace(":", "")
        event2time1, event2time2 = event2[0].replace(":", ""), event2[1].replace(":", "")

        if int(event2time2) < int(event1time1) or int(event2time1) > int(event1time2):
            return False
        
        return True