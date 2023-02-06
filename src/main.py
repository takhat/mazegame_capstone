import pygame, sys
import time
from cell import Cell
from game_state import GameState
from maze_generator import MazeGenerator
from player import Player

# ## setup maze variables
cell_width = 45     #player class also uses cell_width         
cols, rows = 15, 15 #cell class also uses cols, rows

# set up pygame window
width = (cell_width*rows)+(2*cell_width) 
height = (cell_width*rows)+(2*cell_width)
FPS = 60 #Frames Per Second

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
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
player.set_position(mg.grid[0].x, mg.grid[0].y)
all_sprites.draw(canvas)   

# ##### pygame loop #######
gs=GameState(canvas, mg, all_sprites, player, cell_width,move_down=False,move_up=False,move_left=False,move_right=False)

while True:
    gs.main_game()
    # keep running at the right speed
    clock.tick(FPS)
    
    
