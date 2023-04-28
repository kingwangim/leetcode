from sortedcontainers import *
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.top = []
        self.poppedPos = SortedSet()

    def push(self, val: int) -> None:
        if not self.poppedPos:
            pos = len(self.stack)
            self.stack.append(val)
            if pos % self.capacity == 0:
                self.top.append(0)
            else:
                stackPos = len(self.top) - 1
                stackTop = self.top[stackPos]
                self.top[stackPos] = stackTop + 1
        else:
            pos = self.poppedPos.pop(0)
            self.stack[pos] = val
            index = pos // self.capacity
            stackTop = self.top[index]
            self.top[index] = stackTop + 1

    def pop(self) -> int:
        while self.stack and self.poppedPos and self.poppedPos[-1] == len(self.stack) - 1:
            self.stack.pop()
            pos = self.poppedPos.pop()
            if pos % self.capacity == 0:
                self.top.pop()
        if not self.stack:
            return -1
        else:
            pos = len(self.stack) - 1
            val = self.stack[pos]
            self.stack.pop()
            if pos % self.capacity == 0 and self.top:
                self.top.pop()
            elif self.top:
                self.top[-1] -= 1
            return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.top):
            return -1
        stackTop = self.top[index]
        if stackTop < 0:
            return -1
        self.top[index] = stackTop - 1
        pos = index * self.capacity + stackTop
        self.poppedPos.add(pos)
        return self.stack[pos]


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)