import pygame

# ## setup maze variables
CELL_WIDTH = 60    #player class also uses cell_width         
COLS, ROWS = 10, 10 #cell class also uses cols, rows


# # set up pygame window
width = (CELL_WIDTH*ROWS)+(2*CELL_WIDTH) 
height = (CELL_WIDTH*ROWS)+(2*CELL_WIDTH)
CANVAS=pygame.display.set_mode((width, height))
FPS = 60 #Frames Per Second

# Define colours
WHITE = (255, 255, 255)
GREEN = (202,248,128)
BLUE = (2,3,129)
YELLOW = (252,185,0,1)
LIGHTPINK=(255,206,236)
GREY=(169, 184, 195)
