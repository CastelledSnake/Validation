from semantics import *


class OneBitClock(Semantics):
    def initial(self):
        return [0, 1]

    def actions(self, c):
        a = []
        if c == 1:
            a.append(lambda x: [0])
        elif c == 0:
            a.append(lambda x: [1])
        return a

    def execute(self, a, c):
        return a(c)
