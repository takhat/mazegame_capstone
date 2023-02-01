import pygame
import time
import random
from cell import Cell
from maze_generator import MazeGenerator

# set up pygame window
WIDTH = 253
HEIGHT = 255
FPS = 3

# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)

# initalize Pygame
pygame.init()
pygame.mixer.init()
win=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Welcome to the maze game!')
clock = pygame.time.Clock()

## setup maze variables
cell_width = 50           
cols, rows = 5, 5
visited = []
stack = []
solution = {}
grid=[] 
current=None

# mg = MazeGenerator(win=win, grid=None, rows=rows, cols=cols, cell_width=cell_width)
# mg.create_grid()
# mg.draw_grid()
index=0
for row in range(rows):
    for col in range(cols):
        cell = Cell(grid_index=index,row_index=row, col_index=col, cell_width=cell_width)
        grid.append(cell)
        index+=1

current = grid[0]
current.visited=True
next = current.check_neighbors(grid)
if next:
    current=next
    print(f"curr: grid_index: {current.grid_index}")

for cell in grid:
    cell.draw(win)




# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False