from random import randint

class Grid:
    def __init__(self, boardsize):
        self.grid = []
        self.boardsize = 4

        for i in range(0, self.boardsize):
            self.grid.append(list())
            for j in range(0, self.boardsize):
                self.grid[i].append(None)

    def tileIterate(self):
        for i in range(0, self.boardsize):
            for j in range(0, self.boardsize):
                yield (self.grid[i][j], i, j)

    # iterator yielding [(x,y)]
    def getAvailable(self):
        for i, j, tile in self.tileIterate():
            if tile is None:
                yield (i,j)

    # returns a random (x,y) that's available
    def randomAvailableCell(self):
        avail = list(self.getAvailable())
        return avail[randint(0,len(avail)-1)]

