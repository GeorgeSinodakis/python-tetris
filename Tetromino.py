from Tile import tile

class tetromino(tile):
    def __init__(self, index, tilesX, tilesY):

        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        PURPLE = (128, 0, 128)
        ORANGE = (255, 165, 0)
        GREY = (128, 128, 128)
        CYAN = (173, 216, 230)
        TURQUOISE = (64, 224, 208)

        shapes = [
            [ tile(0, 0, CYAN), tile(1,  0, CYAN), tile(2,  0, CYAN), tile(3, 0,  CYAN) ],
            [ tile(0, 0, BLUE), tile(-1, 0, BLUE), tile(-1, 1, BLUE), tile(1, 0,  BLUE) ],
            [ tile(0, 0, ORANGE), tile(-1, 0, ORANGE), tile(1,  1, ORANGE), tile(1, 0,  ORANGE) ],
            [ tile(0, 0, YELLOW), tile(1,  0, YELLOW), tile(0,  1, YELLOW), tile(1, 1,  YELLOW) ],
            [ tile(0, 0, GREEN), tile(-1, 0, GREEN), tile(0,  1, GREEN), tile(1, 1,  GREEN) ],
            [ tile(0, 0, PURPLE), tile(-1, 0, PURPLE), tile(1,  0, PURPLE), tile(0, 1,  PURPLE) ],
            [ tile(0, 0, RED), tile(1,  0, RED), tile(0,  1, RED), tile(-1, 1, RED) ]
        ]

        origins = [
            [1.5, -0.5],
            [0, 0],
            [0, 0],
            [0.5, 0.5],
            [0, 0],
            [0, 0],
            [0, 0]
        ]

        positions = [
            [tilesX/2 - 2, tilesY - 1],
            [tilesX/2 - 1, tilesY - 2],
            [tilesX/2 - 1, tilesY - 2],
            [tilesX/2 - 1, tilesY - 2],
            [tilesX/2 - 1, tilesY - 2],
            [tilesX/2 - 1, tilesY - 2],
            [tilesX/2 - 1, tilesY - 2]
        ]

        self.tiles = shapes[index]
        self.origin = origins[index]

        self.origin[0] += positions[index][0]
        self.origin[1] += positions[index][1]

        for n in self.tiles:
            n.x += positions[index][0]
            n.y += positions[index][1]

    def Rotate(self):
        for n in self.tiles:
            n.Rotate(self.origin)

    def Down(self):
        for n in self.tiles:
            n.Down()
        self.origin[1] -= 1

    def Up(self):
        for n in self.tiles:
            n.Up()
        self.origin[1] += 1

    def Left(self):
        for n in self.tiles:
            n.Left()
        self.origin[0] -= 1

    def Right(self):
        for n in self.tiles:
            n.Right()
        self.origin[0] += 1