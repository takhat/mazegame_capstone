import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    """represents a player sprite."""
    def __init__(self, width, height):
        super().__init__()
        self.image=pygame.Surface((width, height)) #creates a surface of a certain width & height
        self.image.fill((99,12,13))
        self.image.set_alpha(90) # sets transparency level
        self.rect=self.image.get_rect()
    
    def set_position(self, x, y):
        self.rect.x=x
        self.rect.y=y
    

        

