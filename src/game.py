import pygame, sys
import time
from cell import Cell
from game_state import GameState
from maze_generator import MazeGenerator
from player import Player
from constants import *

clock = pygame.time.Clock()

gs= GameState()

##### pygame loop #######
while True:
    gs.state_manager()
    # keep running at the right speed
    clock.tick(FPS+20)
    
    
