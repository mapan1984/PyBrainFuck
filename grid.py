START = 1
END = 2

class Grid:

    def __init__(self):
        self.grids = [0]
        self.index = 0
        self.operation = {
            '<': self.right,
            '>': self.left,
            '+': self.increase,
            '-': self.decrease,
            '.': self.out,
            ',': self.inp,
            '[': self.start,
            ']': self.end,
        }

    def right(self):
        self.index -= 1

    def left(self):
        self.index += 1
        if self.index >= len(self.grids):
            self.grids.append(0)

    def increase(self):
        self.grids[self.index] += 1

    def decrease(self):
        self.grids[self.index] -= 1

    def out(self):
        print(chr(self.grids[self.index]), end='')

    def inp(self):
        self.grids[self.index] = ord(input())

    def start(self):
        if self.grids[self.index] == 0:
            return END

    def end(self):
        return START

    def operate(self, c):
        return self.operation[c]()

