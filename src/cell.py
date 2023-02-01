import random
import pygame

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
cols, rows = 5, 5
class Cell:
    def __init__(self, grid_index, row_index, col_index, cell_width):
        self.grid_index=grid_index
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

        if self.visited:
            pygame.draw.rect(win, BLUE, (self.x+1, self.y+1, self.cell_width-1, self.cell_width-1))
            pygame.display.update()
            print(f"r:{self.row_index}, c:{self.col_index}, visited:{self.visited}")

    def check_neighbors(self, grid):
        neighbors=[]

        if self.grid_index-cols >= 0 and self.grid_index-cols<cols*(rows-1):
            top = grid[self.grid_index-cols]
        else:
            top = None
        if self.grid_index+cols >= 1 and self.grid_index+cols<cols*rows:
            bottom = grid[self.grid_index+cols]
        else:
            bottom=None
        if self.grid_index-1 >= 0:
            left= grid[self.grid_index-1]
        else:
            left=None
        if self.grid_index+1<cols*rows:
            right=grid[self.grid_index+1]
        else:
            right=None

        if top and top.visited is False:
            neighbors.append(top)
            print(f"top grid_index:{top.grid_index} row_index: {top.row_index} col_index:{top.col_index}")
        if bottom and bottom.visited is False:
            neighbors.append(bottom)
            print(f"bottom grid_index:{bottom.grid_index} row_index: {bottom.row_index} col_index:{bottom.col_index}")
        if left and left.visited is False:
            neighbors.append(left)
            print(f"left grid_index:{left.grid_index} row_index: {left.row_index} col_index:{left.col_index}")
        if right and right.visited is False:
            neighbors.append(right)
            print(f"right grid_index:{right.grid_index} row_index: {right.row_index} col_index:{right.col_index}")
        if len(neighbors)>0:
            chosen_neighbor = random.choice(neighbors)
            chosen_neighbor.visited=True

            if chosen_neighbor == top:
                #remove the top wall of current cell, and bottom wall of neighbor
                self.walls["top"]= False
                chosen_neighbor.walls["bottom"]= False
                print(f"removing wall between grid cells {self.grid_index} and {chosen_neighbor.grid_index}")
                print(self.walls["top"])
                print(chosen_neighbor.walls["bottom"])
            if chosen_neighbor == bottom:
                #remove the bottom wall of current cell, and top wall of neighbor
                self.walls["bottom"]= False
                chosen_neighbor.walls["top"]= False
                print(f"removing wall between grid cells {self.grid_index} and {chosen_neighbor.grid_index}")
                print(self.walls["bottom"])
                print(chosen_neighbor.walls["top"])
            if chosen_neighbor == left:
                #remove the left wall of current cell, and right wall of neighbor
                self.walls["left"]= False
                chosen_neighbor.walls["right"]= False
                print(f"removing wall between grid cells {self.grid_index} and {chosen_neighbor.grid_index}")
                print(self.walls["left"])
                print(chosen_neighbor.walls["right"])
            if chosen_neighbor == right:
                #remove the right wall of current cell, and left wall of neighbor
                self.walls["right"]= False
                chosen_neighbor.walls["left"]= False
                print(f"removing wall between grid cells {self.grid_index} and {chosen_neighbor.grid_index}")
                print(self.walls["right"])
                print(chosen_neighbor.walls["left"])
            return chosen_neighbor
    
       