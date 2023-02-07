import pygame, sys
import time
from cell import Cell
from game_state import GameState
from maze_generator import MazeGenerator
from player import Player
from constants import *

clock = pygame.time.Clock()
def initgame():
    # initalize Pygame
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Welcome to the maze game!')
    

    #Maze 
    mg = MazeGenerator(canvas=canvas,rows=ROWS, cols=COLS, cell_width=CELL_WIDTH)
    mg.create_grid() 
    mg.generate_maze()
    mg.draw_maze()

    #Sprite/Player 
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    player.set_position(mg.grid[0].x, mg.grid[0].y)
    all_sprites.draw(canvas)   

    gs=GameState(mg, canvas, all_sprites, player, CELL_WIDTH)
    
    return gs

gs= initgame()

##### pygame loop #######
while True:
    gs.state_manager()
    if gs.state=="restart_game":
        canvas.fill((0,0,0))
        gs=initgame()

    # keep running at the right speed
    clock.tick(FPS)
    
    
