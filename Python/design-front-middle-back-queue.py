class FrontMiddleBackQueue:

    def __init__(self):
        self.queue_list = []

    def pushFront(self, val: int) -> None:
        self.queue_list = [val] + self.queue_list

    def pushMiddle(self, val: int) -> None:
        len_queue = len(self.queue_list)
        if len_queue > 0:
            self.queue_list = self.queue_list[:len_queue //
                                              2] + [val] + self.queue_list[len_queue//2:]
        else:
            self.queue_list.append(val)

    def pushBack(self, val: int) -> None:
        self.queue_list.append(val)

    def popFront(self) -> int:
        if len(self.queue_list) > 0:
            v = self.queue_list[0]
            self.queue_list.remove(v)
            return v
        else:
            return -1

    def popMiddle(self) -> int:
        len_queue = len(self.queue_list)
        if len_queue > 0:
            if len_queue % 2 == 0:
                v = self.queue_list[len_queue//2-1]
                self.queue_list = self.queue_list[:len_queue //
                                                  2-1] + self.queue_list[len_queue//2:]
            else:
                v = self.queue_list[len_queue//2]
                self.queue_list = self.queue_list[:len_queue //
                                                  2] + self.queue_list[len_queue//2+1:]
            return v
        else:
            return -1

    def popBack(self) -> int:
        if len(self.queue_list) > 0:
            v = self.queue_list[-1]
            self.queue_list = self.queue_list[:-1]
            return v
        else:
            return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
