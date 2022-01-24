import random
import sys
import time
import pygame
from Cell import Cell

WIDTH = 800
HEIGHT = 800
FPS = 30
n = 20
len = WIDTH/n
counter = 0
gridcells = [[0 for x in range(n)] for y in range(n)]


# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = (255, 255, 255,255)
black = (0, 0, 0,255)
blue= (0,0,128)
screen.fill(white)
pygame.display.update()


def newgrid():
    temp=n
    i=1
    while i < temp:
        pygame.draw.line(screen, black, (0, (temp - 1) * len), (WIDTH, (temp - 1) * len), 3)
        pygame.draw.line(screen, black, ((temp - 1) * len, 0), ((temp - 1) * len, WIDTH), 3)
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
    for m in range(4):
        if column + 1 < n and gridcells[row][column + 1].visited == 0 and randList[m]==0:
            # move right
            pygame.draw.line(screen, white, (current.x + len, current.y), (current.x + len, current.y - len), 3)
            move(row, column + 1)

        if row + 1 < n and gridcells[row + 1][column].visited == 0 and randList[m]==1:
            # move down
            pygame.draw.line(screen, white, (current.x, current.y), (current.x + len, current.y), 3)
            move(row + 1, column)

        if column - 1 >= 0 and gridcells[row][column - 1].visited == 0 and randList[m]==2:
            # move left
            pygame.draw.line(screen, white, (current.x, current.y), (current.x, current.y - len), 3)
            move(row, column - 1)

        if row - 1 >= 0 and gridcells[row - 1][column].visited == 0 and randList[m]==3:
            # move up
            pygame.draw.line(screen, white, (current.x,current.y-len),(current.x+len,current.y-len), 3)
            move(row - 1,column)

def find_solution(row, column):
    endpoint = gridcells[n-1][n-1]
    current = gridcells[row][column]
    current.visited=2
    randList = random.sample(range(0, 4), 4)
    for m in range(4):
        if column + 1 < n and pygame.Surface.get_at(screen,(current.x+len,current.y-len/2))==white and gridcells[row][column + 1].visited ==1 and randList[m]==0:
            # move right
            gridcells[row][column+1].parent = current
            find_solution(row, column + 1)

        if row + 1 < n and pygame.Surface.get_at(screen,(current.x+len/2,current.y))==white and gridcells[row+1][column].visited ==1 and randList[m] == 1:
            # move down
            gridcells[row+1][column].parent = current
            find_solution(row + 1, column)

        if column - 1 >= 0 and pygame.Surface.get_at(screen,(current.x,current.y-len/2))==white and gridcells[row][column-1].visited ==1 and randList[m] == 2:
            # move left
            gridcells[row][column-1].parent = current
            find_solution(row, column - 1)

        if row - 1 >= 0 and pygame.Surface.get_at(screen,(current.x+len/2,current.y-len))==white and gridcells[row-1][column].visited ==1 and randList[m] == 3:
            # move up
            gridcells[row-1][column].parent = current
            find_solution(row - 1, column)
        if current == endpoint:
            print_solution(endpoint)
            return False




def print_solution(endpoint):
    pygame.display.update()
    time.sleep(0.01)
    pygame.draw.circle(screen, blue, (endpoint.x + len / 2, endpoint.y - len / 2), 5)
    if endpoint == gridcells[0][0]:
        pygame.draw.circle(screen, blue, (gridcells[0][0].x + len / 2, gridcells[0][0].y - len / 2), 5)
        pygame.display.update()
        return False
    print_solution(endpoint.parent)



# create grid
newgrid()
# array of cells
for i in range(n):
    for j in range(n):
        cell = Cell((j*len), (i*len)+len, 0, 0)
        gridcells[i][j] = cell

# create maze using growing tree algorithm
column = random.randint(0, n-1)
row = random.randint(0, n-1)
print row,column

maze_create(0,0)

#find solution
find_solution(0, 0)
print "done"
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

