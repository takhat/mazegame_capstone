import pygame
LIGHTPINK=(255,206,236)
cell_width=60
class Player(pygame.sprite.Sprite):
    """represents a player sprite."""
    def __init__(self, width=cell_width, height = cell_width):
        super().__init__()
        self.image=pygame.Surface((width, height)) #creates a window of a certain width & height
        self.image.fill((10,210,0))
        self.image.set_alpha(80) # sets transparency level
        self.rect=self.image.get_rect()
    
    def set_position(self, x, y):
        self.rect.x=x
        self.rect.y=y
        

