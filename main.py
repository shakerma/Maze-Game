import random
import time
import pygame
from Cell import Cell

WIDTH = 800
HEIGHT = 800
FPS = 30
n =20
len = WIDTH/n
gridcells = [[0 for x in range(n)] for y in range(n)]

# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0, 0, 0]
screen.fill(white)
pygame.display.update()


def newgrid():
    temp=n
    i=1
    while i < temp:
        pygame.draw.line(screen, black, (0, (temp - 1) * len), (WIDTH, (temp - 1) * len), 2)
        pygame.draw.line(screen, black, ((temp - 1) * len, 0), ((temp - 1) * len, WIDTH), 2)
        temp -= 1

def maze_create(row,column):
    current = gridcells[row][column]
    if current.visited == 0:
        move(row, column)


def move (row, column):
    current = gridcells[row][column]
    current.visited = 1
    pygame.display.update()
    time.sleep(0.01)
    randList = random.sample(range(0, 4), 4)
    print randList
    for m in range(4):
        print m
        if column + 1 < n and gridcells[row][column + 1].visited == 0 and randList[m]==0:
            # move right
            pygame.draw.line(screen, white, (current.x + len, current.y), (current.x + len, current.y - len), 2)
            gridcells[row][column + 1].parent = current
            move(row, column + 1)

        if row + 1 < n and gridcells[row + 1][column].visited == 0 and randList[m]==1:
            # move up
            pygame.draw.line(screen, white, (current.x, current.y), (current.x + len, current.y), 2)
            gridcells[row + 1][column].parent = current
            move(row + 1, column)

        if column - 1 >= 0 and gridcells[row][column - 1].visited == 0 and randList[m]==2:
            # move left
            pygame.draw.line(screen, white, (current.x, current.y), (current.x, current.y - len), 2)
            gridcells[row][column - 1].parent = current
            move(row, column - 1)

        if row - 1 >= 0 and gridcells[row - 1][column].visited == 0 and randList[m]==3:
            # move down
            pygame.draw.line(screen, white, (current.x,current.y-len),(current.x+len,current.y-len), 2)
            gridcells[row - 1][column].parent=current
            move(row - 1,column)




# create grid
newgrid()
# array of cells
for i in range(n):
    for j in range(n):
        cell = Cell(len, (j*len), (i*len)+len, 0, 0, 0)
        gridcells[i][j] = cell

# create maze using growing tree algorithm
column = random.randint(0, n-1)
row = random.randint(0, n-1)

# print row,column
maze_create(row,column)




running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

