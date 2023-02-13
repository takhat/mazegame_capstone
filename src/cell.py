import pygame, random, time
from constants import *

class Cell:
    def __init__(self, grid_index, row_index, col_index, cell_width, level):
        self.grid_index=grid_index
        self.row_index=row_index
        self.col_index=col_index
        self.cell_width=cell_width
        self.visited=False
        self.rows=rows*level
        self.cols=cols*level
        self.level=level
        self.walls={
            "left": True,
            "right": True,
            "top":True,
            "bottom": True
        }
        if self.grid_index==0:
            self.walls["left"]=False

        if self.grid_index==self.rows*self.cols-1:
            self.walls["right"]=False   
        
        self.x = (self.col_index*self.cell_width)+self.cell_width
        self.y = (self.row_index*self.cell_width)+self.cell_width
        self.is_dfs_cell=False
        self.is_solution_cell=False

    def draw(self):
        """draws the walls of each cell."""
        if self.visited:
            pygame.draw.rect(CANVAS, ADACOLORS[self.level-1], (self.x, self.y, self.cell_width, self.cell_width))
        
        if self.is_solution_cell:
            pygame.draw.rect(CANVAS, GREEN, (self.x+3, self.y+3, 3, 3))

        # if self.is_dfs_cell:
        #     pygame.draw.rect(CANVAS, GREEN, (self.x+3, self.y+3, 3, 3))

        if self.walls["left"]:
            #line(surface, color, start_pos, end_pos)
            pygame.draw.line(CANVAS, WHITE, (self.x, self.y),(self.x,self.y+self.cell_width))

        if self.walls["right"]:
            pygame.draw.line(CANVAS, WHITE, (self.x+self.cell_width, self.y),(self.x+self.cell_width,self.y+self.cell_width))

        if self.walls["top"]:
            pygame.draw.line(CANVAS, WHITE, (self.x, self.y),(self.x+self.cell_width, self.y))

        if self.walls["bottom"]:
            pygame.draw.line(CANVAS, WHITE, (self.x, self.y+self.cell_width),(self.x+self.cell_width,self.y+self.cell_width))


    def get_random_unvisited_neighbor(self, grid):
        """returns an unvisited neighbor chosen randomly. Removes walls between current cell and chosen neighbor."""
        neighbors=[]

        if self.row_index==0:
            top = None
        else:
            top = grid[self.grid_index-self.cols]

        if self.row_index==self.rows-1:
            bottom=None
        else:
            bottom = grid[self.grid_index+self.cols]
      
        if self.col_index == 0:
            left=None
        else:
            left= grid[self.grid_index-1]

        if self.col_index >= self.cols-1:
            right=None
        else:
            right=grid[self.grid_index+1]
            
        if top and top.visited == False:
            neighbors.append(top)
            # print(f"top grid_index:{top.grid_index} row_index: {top.row_index} col_index:{top.col_index}")
        if bottom and bottom.visited == False:
            neighbors.append(bottom)
            # print(f"bottom grid_index:{bottom.grid_index} row_index: {bottom.row_index} col_index:{bottom.col_index}")
        if left and left.visited == False:
            neighbors.append(left)
            # print(f"left grid_index:{left.grid_index} row_index: {left.row_index} col_index:{left.col_index}")
        if right and right.visited == False:
            neighbors.append(right)
            # print(f"right grid_index:{right.grid_index} row_index: {right.row_index} col_index:{right.col_index}")
        
        if len(neighbors)>0:
            chosen_neighbor = random.choice(neighbors)
            if chosen_neighbor == top:
                #remove the top wall of current cell, and bottom wall of neighbor
                self.walls["top"]= False
                chosen_neighbor.walls["bottom"]= False
                # print(f"removing wall between grid cells {self.grid_index} and {chosen_neighbor.grid_index}")

            if chosen_neighbor == bottom:
                #remove the bottom wall of current cell, and top wall of neighbor
                self.walls["bottom"]= False
                chosen_neighbor.walls["top"]= False
                # print(f"removing wall between grid cells {self.grid_index} and {chosen_neighbor.grid_index}")

            if chosen_neighbor == left:
                #remove the left wall of current cell, and right wall of neighbor
                self.walls["left"]= False
                chosen_neighbor.walls["right"]= False
                # print(f"removing wall between grid cells {self.grid_index} and {chosen_neighbor.grid_index}")

            if chosen_neighbor == right:
                #remove the right wall of current cell, and left wall of neighbor
                self.walls["right"]= False
                chosen_neighbor.walls["left"]= False
                # print(f"removing wall between grid cells {self.grid_index} and {chosen_neighbor.grid_index}")
          
            return chosen_neighbor



    




            
    
       