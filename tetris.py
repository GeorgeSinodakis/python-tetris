import pygame
import math as m
import random
from itertools import filterfalse

pygame.init()

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

nodeSize = 20
nodesX = 10
nodesY = 25

screen = pygame.display.set_mode([nodesX * nodeSize, nodesY * nodeSize])
pygame.display.set_caption("Tetris")

bucket = []
index = 0
currentObject = 0

class node:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveLeft(self):
        self.x -= 1

    def moveRight(self):
        self.x += 1

    def rotateClockwise(self, origin):

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

    def rotateCounterClockwise(self, origin):

        #offset the point
        self.x -= origin[0]
        self.y -= origin[1]

        #calculate the rotation
        newX = -self.y
        newY = self.x

        #return the data
        newX += origin[0]
        newY += origin[1]
        
        self.x = newX
        self.y = newY

class shape:
    def __init__(self):

        global index

        shapes = [
            [ node(0, 0, CYAN), node(1,  0, CYAN), node(2,  0, CYAN), node(3, 0,  CYAN) ],
            [ node(0, 0, BLUE), node(-1, 0, BLUE), node(-1, 1, BLUE), node(1, 0,  BLUE) ],
            [ node(0, 0, ORANGE), node(-1, 0, ORANGE), node(1,  1, ORANGE), node(1, 0,  ORANGE) ],
            [ node(0, 0, YELLOW), node(1,  0, YELLOW), node(0,  1, YELLOW), node(1, 1,  YELLOW) ],
            [ node(0, 0, GREEN), node(-1, 0, GREEN), node(0,  1, GREEN), node(1, 1,  GREEN) ],
            [ node(0, 0, PURPLE), node(-1, 0, PURPLE), node(1,  0, PURPLE), node(0, 1,  PURPLE) ],
            [ node(0, 0, RED), node(1,  0, RED), node(0,  1, RED), node(-1, 1, RED) ]
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

        self.nodes = shapes[index]
        self.origin = origins[index]

        if index == 6:
            index = 0
        else:
            index += 1

        self.origin[0] += nodesX/2
        self.origin[1] += nodesY - 5

        for n in self.nodes:
            n.x += nodesX/2
            n.y += nodesY - 5

    def rotateClockwise(self):
        for n in self.nodes:
            n.rotateClockwise(self.origin)

    def rotateCounterClockwise(self):
       for n in self.nodes:
            n.rotateCounterClockwise(self.origin)

    def Down(self):
        for n in self.nodes:
            n.moveDown()
        self.origin[1] -= 1

    def Up(self):
        for n in self.nodes:
            n.moveUp()
        self.origin[1] += 1

    def Left(self):
        for n in self.nodes:
            n.moveLeft()
        self.origin[0] -= 1

    def Right(self):
        for n in self.nodes:
            n.moveRight()
        self.origin[0] += 1

def collision():
    global bucket
    global currentObject

    for n1 in bucket:
        for n2 in currentObject.nodes:
            if n1 == n2:
                return True
    return False

def outOfBounds():
    global bucket
    global currentObject

    for n in currentObject.nodes:
        if n.y < 0:
            return True
        if n.x < 0:
            return True
        if n.x > nodesX - 1:
            return True
    
def goDown():
    global bucket
    global currentObject

    currentObject.Down()
    if collision() or outOfBounds():
        currentObject.Up()
        return False
    return True

def goLeft():
    global bucket
    global currentObject

    currentObject.Left()
    if collision() or outOfBounds():
        currentObject.Right()
        return False
    return True

def goRight():
    global bucket
    global currentObject

    currentObject.Right()
    if collision() or outOfBounds():
        currentObject.Left()
        return False
    return True    

def clearLines():
    global bucket
    global currentObject

    for line in range(0, nodesY):
        if sum(1 for n in bucket if n.y == line) == nodesX:
            for n in bucket[:]:
                if n.y == line:
                    bucket.remove(n)
                if n.y > line:
                    n.moveDown()
            

def drawNode(n):
    xn = n.x * nodeSize
    yn = (nodesY - 1) * nodeSize - n.y * nodeSize
    pygame.draw.rect(screen, n.color, (xn, yn, nodeSize, nodeSize), 0)

def draw():
    global bucket
    global currentObject

    screen.fill(BLACK)

    for n in bucket:
        drawNode(n)

    for n in currentObject.nodes:
        drawNode(n)

def update():
    global bucket
    global currentObject

    if not goDown():
        for n in currentObject.nodes:
            bucket.append(n)
        currentObject = None
        currentObject = shape()

    if sum(1 for n in bucket if n.y > nodesY/2):
        init()

    clearLines()
        
def userInput():
    global bucket
    global currentObject

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                currentObject.rotateClockwise()
            if event.key == pygame.K_b:
                currentObject.rotateCounterClockwise()
            if event.key == pygame.K_LEFT:
                goLeft()
            if event.key == pygame.K_RIGHT:
                goRight()
            if event.key == pygame.K_DOWN:
                goDown()
    return True

def init():
    global bucket
    global currentObject
    global index

    bucket = []
    index = 0
    currentObject = shape()

init()
a = 0
while userInput():
    a += 1
    if a == 300:
        update()
        a = 0
    draw()
    pygame.display.flip()

pygame.quit()
