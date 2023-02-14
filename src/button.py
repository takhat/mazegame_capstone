import pygame
from constants import *

pygame.init()
font=pygame.font.SysFont("arial", 14, bold=True)
class Button:
    def __init__(self,text,x,y):
        self.x=x
        self.y=y
        self.set(text)

    def draw(self, canvas, coord=(1,1)):
        canvas.blit(self.canvas,coord)
        pygame.display.update()

    def set(self, text):
        self.text=font.render(text, 1, pygame.Color(WHITE))
        size = w, h = self.text.get_size()
        self.rect=pygame.Rect(self.x,self.y, w, h)
        self.canvas=pygame.Surface(size)
        self.canvas.fill(DARKPINK)
        self.canvas.blit(self.text,(1,1))
        pygame.display.update()

        
