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
FPS = 5

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

#cell_dict to use for collisions
grid=mg.grid
cell_dict={}
for cell in grid:
    cell_dict[(cell.x, cell.y)]=cell

#Sprite/Player 
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
player.set_position(mg.grid[0].x, mg.grid[0].y)
all_sprites.draw(canvas)   

# ##### pygame loop #######
gs=GameState(canvas, mg.grid, all_sprites, player, cell_width)
running = True

move_down=False
move_up=False
move_left=False
move_right=False

while running:
    # mg.draw_maze()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right=True
            if event.key == pygame.K_LEFT:
                move_left=True
            if event.key == pygame.K_UP:
                move_up=True
            if event.key == pygame.K_DOWN:
                move_down=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right=False
            if event.key == pygame.K_LEFT:
                move_left=False
            if event.key == pygame.K_UP:
                move_up=False
            if event.key == pygame.K_DOWN:
                move_down=False

    if move_right:
        print("right key pressed")
        x=player.rect.x
        y=player.rect.y
        current_cell = cell_dict[(x,y)]
        if current_cell.walls["right"]:
            print("movement not allowed")
        else:
            player.set_position(x+cell_width, y)
            print(player.rect.x, player.rect.y)
            print(f"grid_index:{cell_dict[(player.rect.x,player.rect.y)].grid_index}")
            mg.draw_maze()
            all_sprites.draw(canvas)  
            pygame.display.update()
    if move_left:
        print("left key pressed")
        x=player.rect.x
        y=player.rect.y
        current_cell = cell_dict[(x,y)]
        if current_cell.walls["left"]:
            print("movement not allowed")
        else:
            player.set_position(player.rect.x-cell_width, player.rect.y)
            print(player.rect.x, player.rect.y)
            print(f"grid_index:{cell_dict[(player.rect.x,player.rect.y)].grid_index}")
            mg.draw_maze()
            all_sprites.draw(canvas) 
    if move_up:
        print("up key pressed")
        x=player.rect.x
        y=player.rect.y
        current_cell = cell_dict[(x,y)]
        if current_cell.walls["top"]:
            print("movement not allowed")
        else:
            player.set_position(player.rect.x, player.rect.y-cell_width)
            print(player.rect.x, player.rect.y)
            print(f"grid_index:{cell_dict[(player.rect.x,player.rect.y)].grid_index}")
            mg.draw_maze()
            all_sprites.draw(canvas) 
    if move_down:
        print("down key pressed")
        x=player.rect.x
        y=player.rect.y
        current_cell = cell_dict[(x,y)]
        if current_cell.walls["bottom"]:
            print("movement not allowed")
        else:
            player.set_position(player.rect.x, player.rect.y+cell_width)
            print(player.rect.x, player.rect.y)
            print(f"grid_index:{cell_dict[(player.rect.x,player.rect.y)].grid_index}")
            mg.draw_maze()
            all_sprites.draw(canvas) 
    pygame.display.flip()
        
    # keep running at the right speed
    clock.tick(FPS)
    
    
