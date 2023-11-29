class SmallestInfiniteSet:

    def __init__(self):
        self.int_remove_list = []
        self.int_add_list = []

    def popSmallest(self) -> int:
        if len(self.int_remove_list) == 0:
            self.int_remove_list.append(1)
            return 1
        else:
            if len(self.int_add_list) != 0:
                v1 = min(self.int_add_list)
                self.int_add_list.remove(v1)
                return v1
            else:
                v = max(self.int_remove_list) + 1
                self.int_remove_list.append(v)
                return v

    def addBack(self, num: int) -> None:
        if num in self.int_remove_list:
            self.int_add_list.append(num)
            self.int_add_list = list(set(self.int_add_list))


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
