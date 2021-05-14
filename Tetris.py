from Tetromino import tetromino
import random

class tetris(tetromino):
    def __init__(self, sqX, sqY):
        self.tilesX = sqX
        self.tilesY = sqY
        self.bucket = []
        self.cTetromino = 0
        self.index = 0
        self.bag = [0, 1, 2, 3, 4, 5, 6]
        self.newTetromino()

    def newTetromino(self):
        if self.index == 7:
            a = [0, 1, 2, 3, 4, 5, 6]
            for i in range(7):
                k = a[random.randint(0, len(a) - 1)]
                self.bag[i] = k
                a.remove(k)
            self.index = 0
        
        self.cTetromino = tetromino(self.bag[self.index], self.tilesX, self.tilesY)
        self.index += 1

    def reset(self):
        self.bucket = []
        self.newTetromino() 

    def collision(self):
        for n1 in self.bucket:
            for n2 in self.cTetromino.tiles:
                if n1 == n2:
                    return True
        return False

    def outOfBounds(self):
        for n in self.cTetromino.tiles:
            if n.y < 0:
                return True
            if n.x < 0:
                return True
            if n.x > self.tilesX - 1:
                return True
        return False
    
    def Rotate(self):
        self.cTetromino.Rotate()
        if self.collision() or self.outOfBounds():
            self.cTetromino.Rotate()
            self.cTetromino.Rotate()
            self.cTetromino.Rotate()

    def DownFast(self):
        while not (self.collision() or self.outOfBounds()):
            self.cTetromino.Down()
        self.cTetromino.Up()
        
    def Down(self):
        self.cTetromino.Down()
        if self.collision() or self.outOfBounds():
            self.cTetromino.Up()
            return False
        return True

    def Left(self):
        self.cTetromino.Left()
        if self.collision() or self.outOfBounds():
            self.cTetromino.Right()

    def Right(self):
        self.cTetromino.Right()
        if self.collision() or self.outOfBounds():
            self.cTetromino.Left()  

    def clearLines(self):
        for line in range(0, self.tilesY):
            if sum(1 for n in self.bucket if n.y == line) == self.tilesX:
                for n in self.bucket[:]:
                    if n.y == line:
                        self.bucket.remove(n)
                    if n.y > line:
                        n.Down()
                
    def update(self):
        if not self.Down():
            for n in self.cTetromino.tiles:
                self.bucket.append(n)
            self.newTetromino()

        if sum(1 for n in self.bucket if n.y > self.tilesY-3):
            self.reset()

        self.clearLines()