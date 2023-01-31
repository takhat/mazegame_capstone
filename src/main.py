import pygame
import time
import random
from cell import Cell
from maze_generator import MazeGenerator

# set up pygame window
WIDTH = 505
HEIGHT = 550
FPS = 30

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
cols, rows = 10, 10
visited = []
stack = []
solution = {}

mg = MazeGenerator(win=win, grid=None, rows=rows, cols=cols, cell_width=cell_width)
mg.create_grid()
mg.draw_grid()

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