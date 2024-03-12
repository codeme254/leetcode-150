class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = None
        self.mins = []

    def push(self, val: int) -> None:
        """
        pushes an element into the stack

        Args:
          val: value to be added into the stack
        """
        if self.min_value == None:
            self.min_value = val
            self.mins.append(self.min_value)
        else:
            if val <= self.min_value:
                self.min_value = val
                self.mins.append(self.min_value)
        self.stack.append(val)

    def pop(self) -> None:
        """
        remove an element on the top of stack
        """
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.min_value = None
            self.mins = []
        elif removed == self.min_value:
            self.mins.pop()
            self.min_value = self.mins[len(self.mins)-1]

    def top(self) -> int:
        """
        gets the top element of the stack

        Returns:
          the top element of the stack
        """
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        """
        retrieves the minimum element in the stack
        """
        return self.min_value

s = MinStack()
s.push(23)
s.push(12)
s.push(32)
s.push(19)
s.push(7)
s.push(65)
s.push(33)
s.push(1)
s.push(1)
s.push(1)
s.push(2)

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()

# s = MinStack()
# s.push(-2)
# s.push(0)
# s.push(-3)
# s.pop()
print(s.top())
print(f"stack: {s.stack}")
print(f"mins: {s.mins}")
print(f"min value: {s.min_value}")