class MinStack:

    def __init__(self):
        #main stack
        self.stack = []

        #stack to track minimums
        self.minStack = []

    def push(self, val: int) -> None:
        # 1. push val into main stack
        self.stack.append(val)
        # 2. compute current minimum
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        # pop from BOTH stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # return top of main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return top of minStack
        return self.minStack[-1]
