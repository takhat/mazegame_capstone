import random
import pygame

# Define colours
WHITE = (255, 255, 255)
GREEN = (202,248,128)#(0, 208, 130)
BLUE = (2,3,129)
YELLOW = (252,185,0,1)
LIGHTPINK=(255,206,236)
GREY=(169, 184, 195)

cols, rows = 15, 15

class Cell:
    def __init__(self, grid_index, row_index, col_index, cell_width):
        self.grid_index=grid_index
        self.row_index=row_index
        self.col_index=col_index
        self.cell_width=cell_width
        self.visited=False
        self.walls={
            "left": True,
            "right": True,
            "top":True,
            "bottom": True
        }
        if self.grid_index==0:
            self.walls["left"]=False

        if self.grid_index==rows*cols-1:
            self.walls["right"]=False   

    def draw(self, canvas):
        """draws the walls of each cell."""
        self.x = (self.col_index*self.cell_width)+self.cell_width
        self.y = (self.row_index*self.cell_width)+self.cell_width

        if self.walls["left"]:
            #line(surface, color, start_pos, end_pos)
            pygame.draw.line(canvas, WHITE, (self.x, self.y),(self.x,self.y+self.cell_width))
            pygame.display.update()
        if self.walls["right"]:
            pygame.draw.line(canvas, WHITE, (self.x+self.cell_width, self.y),(self.x+self.cell_width,self.y+self.cell_width))
            pygame.display.update()
        if self.walls["top"]:
            pygame.draw.line(canvas, WHITE, (self.x, self.y),(self.x+self.cell_width, self.y))
            pygame.display.update()
        if self.walls["bottom"]:
            pygame.draw.line(canvas, WHITE, (self.x, self.y+self.cell_width),(self.x+self.cell_width,self.y+self.cell_width))
            pygame.display.update()

        if self.visited:
            pygame.draw.rect(canvas, BLUE, (self.x+1, self.y+1, self.cell_width-1, self.cell_width-1))
            pygame.display.update()

    def get_random_unvisited_neighbor(self, grid):
        """returns an unvisited neighbor chosen randomly. Removes walls between current cell and chosen neighbor."""
        neighbors=[]

        if self.row_index==0:
            top = None
        else:
            top = grid[self.grid_index-cols]

        if self.row_index==rows-1:
            bottom=None
        else:
            bottom = grid[self.grid_index+cols]
      
        if self.col_index == 0:
            left=None
        else:
            left= grid[self.grid_index-1]

        if self.col_index >= cols-1:
            right=None
        else:
            right=grid[self.grid_index+1]
            
        if top and top.visited == False:
            neighbors.append(top)
            print(f"top grid_index:{top.grid_index} row_index: {top.row_index} col_index:{top.col_index}")
        if bottom and bottom.visited == False:
            neighbors.append(bottom)
            print(f"bottom grid_index:{bottom.grid_index} row_index: {bottom.row_index} col_index:{bottom.col_index}")
        if left and left.visited == False:
            neighbors.append(left)
            print(f"left grid_index:{left.grid_index} row_index: {left.row_index} col_index:{left.col_index}")
        if right and right.visited == False:
            neighbors.append(right)
            print(f"right grid_index:{right.grid_index} row_index: {right.row_index} col_index:{right.col_index}")
        
        if len(neighbors)>0:
            chosen_neighbor = random.choice(neighbors)

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


    




            
    
       