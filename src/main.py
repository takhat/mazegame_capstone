import pygame
import time
import random
from cell import Cell
from maze_generator import MazeGenerator

# set up pygame window
WIDTH = 505
HEIGHT = 505
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
cols, rows = 10,10
visited = []
stack = []
solution = {}
grid=[] 
current=None
stack=[]

# mg = MazeGenerator(win=win, grid=None, rows=rows, cols=cols, cell_width=cell_width)
# mg.create_grid()
# mg.draw_grid()

# Choose the initial cell, mark it as visited and push it to the stack
# While the stack is not empty
# Pop a cell from the stack and make it a current cell
# If the current cell has any neighbours which have not been visited
# Push the current cell to the stack
# Choose one of the unvisited neighbours
# Remove the wall between the current cell and the chosen cell
# Mark the chosen cell as visited and push it to the stack
index=0
for row in range(rows):
    for col in range(cols):
        cell = Cell(grid_index=index,row_index=row, col_index=col, cell_width=cell_width)
        grid.append(cell)
        index+=1

# Choose the initial cell, mark it as visited and push it to the stack

current = grid[0]
current.visited=True
visited.append(current)
stack.append(current)

# While the stack is not empty
while len(stack)>0:
    # Pop a cell from the stack and make it a current cell
    current=stack.pop()
    # If the current cell has any neighbours which have not been visited
    chosen = current.get_random_unvisited_neighbor(grid) # Choose one of the unvisited neighbours
    if chosen:                         # Remove the wall between the current cell and the chosen cell
    # Push the current cell to the stack
        stack.append(current)
        # Mark the chosen cell as visited and push it to the stack
        chosen.visited=True
        visited.append(chosen)
        stack.append(chosen)


for cell in grid:
    cell.draw(win)

for cell in visited:
    print(cell.grid_index)

# ##### pygame loop #######
running = True
while running:
    # keep running at the right speed
    clock.tick(FPS)
    
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False