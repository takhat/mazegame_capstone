import pygame

WHITE = (255, 255, 255)

class Cell:
    def __init__(self, row_index, col_index, cell_width):
        self.row_index=row_index
        self.col_index=col_index
        self.cell_width=cell_width
        self.walls={
            "left": True,
            "right": True,
            "top":True,
            "bottom": True
        }
        self.neighbors={
            "left": None,
            "right": None,
            "top": None,
            "bottom": None
        }
        self.visited=False

    def draw(self, win):
        self.x = self.col_index*self.cell_width
        self.y = self.row_index*self.cell_width

        if self.walls["left"]:
            #line(surface, color, start_pos, end_pos)
            pygame.draw.line(win, WHITE, (self.x, self.y),(self.x,self.y+self.cell_width))
            pygame.display.update()
        if self.walls["right"]:
            pygame.draw.line(win, WHITE, (self.x+self.cell_width, self.y),(self.x+self.cell_width,self.y+self.cell_width))
            pygame.display.update()
        if self.walls["top"]:
            pygame.draw.line(win, WHITE, (self.x, self.y),(self.x+self.cell_width, self.y))
            pygame.display.update()
        if self.walls["bottom"]:
            pygame.draw.line(win, WHITE, (self.x, self.y+self.cell_width),(self.x+self.cell_width,self.y+self.cell_width))
            pygame.display.update()
        


       