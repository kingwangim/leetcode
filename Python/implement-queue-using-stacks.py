class MyQueue:

    def __init__(self):
        self.res = []

    def push(self, x: int) -> None:
        self.res.append(x)

    def pop(self) -> int:
        ans = self.res[0]
        self.res.remove(ans)
        return ans

    def peek(self) -> int:
        ans = self.res[0]
        return ans

    def empty(self) -> bool:
        if len(self.res) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()