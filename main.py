import pygame
import Tetris

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

squareSize = 20
squaresX = 10
squaresY = 30

winDimentions = [squaresX * squareSize + squaresX-1, 
                squaresY * squareSize + squaresY-1]

pygame.init()
screen = pygame.display.set_mode(winDimentions)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 700)


Game = Tetris.tetris(squaresX, squaresY)


def drawtile(n):
    xn = n.x * (squareSize+1)
    yn = (squaresY - 1) * (squareSize+1) - n.y * (squareSize+1)
    pygame.draw.rect(screen, n.color, (xn, yn, squareSize, squareSize), 0)

def drawLines():
    for x in range(1, squaresX + 1):
        start = [x * squareSize + x - 1, 0]
        end = [x * squareSize + x - 1, winDimentions[1]]
        pygame.draw.line(screen, (50,50,50), start, end)

    for y in range(1, squaresY + 1):
        start = [0, y*squareSize + y - 1]
        end = [winDimentions[0], y*squareSize + y - 1]
        pygame.draw.line(screen, (50,50,50), start, end)

def draw():

    screen.fill(BLACK)

    for n in Game.bucket:
        drawtile(n)

    for n in Game.cTetromino.tiles:
        drawtile(n)

    drawLines()


def userInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Game.Rotate()
            if event.key == pygame.K_LEFT:
                Game.Left()
            if event.key == pygame.K_RIGHT:
                Game.Right()
            if event.key == pygame.K_DOWN:
                Game.Down()
            if event.key == pygame.K_SPACE:
                Game.DownFast()
        if event.type == pygame.USEREVENT:
            Game.update()
    return True


def Main():
    while userInput():
        draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    Main()
