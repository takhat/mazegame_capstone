import pygame, sys
import time
from cell import Cell
from game_state import GameState
from maze_generator import MazeGenerator
from player import Player

# ## setup maze variables
cell_width = 60            
cols, rows = 10, 10

# set up pygame window
width = (cell_width*rows)+(2*cell_width) 
height = (cell_width*rows)+(2*cell_width)
FPS = 30

# initalize Pygame
pygame.init()
pygame.mixer.init()
canvas=pygame.display.set_mode((width, height))
pygame.display.set_caption('Welcome to the maze game!')
clock = pygame.time.Clock()

mg = MazeGenerator(canvas=canvas,rows=rows, cols=cols, cell_width=cell_width)
mg.create_grid()
mg.generate_maze()
mg.draw_maze()

#Sprite/Player 
sprite_group = pygame.sprite.Group()
player = Player()
player.set_position(cell_width*3, cell_width*4)
sprite_group.add(player)
sprite_group.draw(canvas)

# ##### pygame loop #######
gs=GameState()
running = True
while running:
    gs.main_game()
    # keep running at the right speed
    clock.tick(FPS)
    
    
