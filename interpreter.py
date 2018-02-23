from grid import Grid, START, END


class Interpreter:
    '''
    BrainFuck Interpreter

    Example:

    >>> code = '+++++[>+++++++++++++<-]>.'
    >>> Interpreter(code).run()
    A
    >>> code = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
    >>> Interpreter(code).run()
    Hello World!
    >>> code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    >>> Interpreter(code).run()
    Hello World!
    '''

    def __init__(self, program):
        self.grid = Grid()
        self.program = program
        self.point = 0

    @property
    def cur(self):
        return self.program[self.point]

    def run(self):
        while True:
            try:
                c = self.cur
            except:
                break
            ret = self.grid.operate(c)

            if ret == START:  # 从`]`回到对应的`[`
                jump = 0
                while True:
                    cur = self.cur
                    if cur == ']':
                        jump += 1
                    elif cur == '[':
                        jump -= 1
                    if jump == 0:
                        break
                    self.point -= 1
            elif ret == END:  # 从'['跳过对应的`]`
                jump = 0
                while True:
                    cur = self.cur
                    if cur == '[':
                        jump += 1
                    elif cur == ']':
                        jump -= 1
                    if jump == 0:
                        break
                    self.point += 1
                self.point += 1
            else:
                self.point += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

