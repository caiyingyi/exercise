# -*- coding:utf8 -*-
class SpiralSquare(object):
    def __init__(self, start, n):
        self.n = n
        self.start = start
        self.square = [[0] * n for i in range(n)]

        self.length = len(str(self.n * self.n)) + 1

    def dfs(self, x=0, y=0):
        if self.n <= 0:
            return
        if self.n == 1:
            self.square[x][y] = self.start

        else:
            # up
            for i in range(self.n):
                self.square[x][y + i] = self.start
                self.start += 1
            # right
            for i in range(self.n - 1):
                self.square[x + 1 + i][y + self.n - 1] = self.start
                self.start += 1
            # down
            for i in range(self.n - 1):
                self.square[x + self.n - 1][y + self.n - 2 - i] = self.start
                self.start += 1
            # left
            for i in range(self.n - 2):
                self.square[x + self.n - 2 - i][y] = self.start
                self.start += 1
            self.n = self.n - 2
            self.dfs(x + 1, y + 1)

        return self.square

    def __repr__(self):
        result = ''
        rule = '%' + str(self.length) + 'd'
        for line in self.square:
            result = result + rule * len(line) % tuple(line) + "\n"
        return result


number = int(raw_input('number:'))
square = SpiralSquare(1, number)
square.dfs()
print square
