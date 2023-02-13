import pygame

# setup maze variables
cols, rows = 3, 3          #cell class also uses cols, rows

# set up pygame window
width=580
height=580    
CANVAS=pygame.display.set_mode((width, height))

FPS = 15 #Frames Per Second

# Define colours
WHITE = (255, 255, 255)
GREEN = (202,248,128)
BLUE = (2,3,129)
YELLOW = (252,185,0,1)
LIGHTPINK=(255,206,236)
GREY=(169, 184, 195)
DARKPINK=(232, 15, 94)
ORANGE=(239, 101, 72)
LIGHTBLUE=(10, 163, 194)
ADACOLORS=[BLUE, ORANGE, LIGHTBLUE]