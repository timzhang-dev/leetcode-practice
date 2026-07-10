class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_2:
            self.stack_2.append(val)
        elif val < self.stack_2[-1]:
            self.stack_2.append(val)
        else:
            self.stack_2.append(self.stack_2[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.stack_2.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_2[-1]
