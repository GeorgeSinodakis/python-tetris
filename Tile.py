class tile:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def Up(self):
        self.y += 1

    def Down(self):
        self.y -= 1

    def Left(self):
        self.x -= 1

    def Right(self):
        self.x += 1

    def Rotate(self, origin):

        #offset the point
        self.x -= origin[0]
        self.y -= origin[1]

        #calculate the rotation
        newX = self.y
        newY = -self.x

        #return the data
        newX += origin[0]
        newY += origin[1]
        
        self.x = newX
        self.y = newY