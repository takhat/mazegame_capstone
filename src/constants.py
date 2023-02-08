import pygame

# ## setup maze variables
cell_width = 50    #player class also uses cell_width         
cols, rows = 4, 4 #cell class also uses cols, rows


# # set up pygame window
width = (cell_width*rows)+(2*cell_width) 
height = (cell_width*rows)+(2*cell_width)
CANVAS=pygame.display.set_mode((width, height))
FPS = 60 #Frames Per Second

# Define colours
WHITE = (255, 255, 255)
GREEN = (202,248,128)
BLUE = (2,3,129)
YELLOW = (252,185,0,1)
LIGHTPINK=(255,206,236)
GREY=(169, 184, 195)
