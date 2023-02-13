import pygame
from cell import Cell
from constants import *

class MazeGenerator:
    """helps to create and position cells inside a grid, and generate and draw a maze from the grid."""
    def __init__(self, rows, cols, cell_width, level):
        self.level=level
        self.rows=rows*level
        self.cols=cols*level
        self.cell_width=cell_width
        self.grid=[]
        self.visited=[]
        self.stack=[]
        self.cell_dict={}
    
    def create_grid(self):
        """makes cells and positions them in a 1D list called grid."""
        index=0
        for row in range(self.rows):
            for col in range(self.cols):
                cell = Cell(grid_index=index,row_index=row, col_index=col, cell_width=self.cell_width,level=self.level)
                self.grid.append(cell)
                index+=1
        
    def generate_maze(self):
        """generates a maze using randomized depth first search (Randomized DFS)."""
        # Choose the initial cell, mark it as visited and push it to the stack
        initial = self.grid[self.cols-1]
        initial.visited=True
        self.visited.append(initial)
        self.stack.append(initial)

        # While the stack is not empty
        while len(self.stack)>0:
            # Pop a cell from the stack and make it a current cell
            current=self.stack.pop()
            # If the current cell has any neighbours which have not been visited
            chosen = current.get_random_unvisited_neighbor(self.grid) # Choose one of the unvisited neighbours
            if chosen:   # Remove the wall between the current cell and the chosen cell
            # Push the current cell to the stack
                self.stack.append(current)
                # Mark the chosen cell as visited and push it to the stack
                chosen.visited=True
                self.visited.append(chosen)
                self.stack.append(chosen)
        #print(self.solution)
    def draw_maze(self):  
        """draws the maze."""
        for cell in self.grid:
            cell.draw()
            self.cell_dict[(cell.x, cell.y)] = cell

        
    # def draw_solution(self, x, y): # draw a small rect starting from the last cell's x,y coordinates
    #     while (x, y) != (self.cell_width, self.cell_width):
    #         if (x, y) in self.cell_dict:
    #             cell = self.cell_dict[(x, y)]
    #             cell.is_solution_cell=True
    #             cell.draw()
    #         (x, y) = self.solution[(x, y)] #new value of x and y = prev cell's x, y coordinates
    #         if (x, y) == (self.cell_width, self.cell_width):
    #             cell = self.cell_dict[(x, y)]
    #             cell.is_solution_cell=True
    #             cell.draw()

            


    def draw_solution_DFS(self):
        dfs_path={}
        start = self.grid[-1]
        explored={start}
        frontier=[start]
        while len(frontier)>0:
            curr_cell=frontier.pop()
            if curr_cell==self.grid[0]:
                break
            print(f"curr cell:{curr_cell.grid_index}")
            for d in ["left", "bottom", "top", "right"]:
                child_cell=None
                if d=="left" and not curr_cell.walls["left"] and curr_cell.grid_index>0:
                    child_cell=self.grid[curr_cell.grid_index-1]
                    print(f"left child: {child_cell.grid_index}")
                if d=="bottom" and not curr_cell.walls["bottom"]:
                    child_cell=self.grid[curr_cell.grid_index+self.cols]
                    print(f"bottom child: {child_cell.grid_index}")
                if d=="top" and not curr_cell.walls["top"]:
                    child_cell=self.grid[curr_cell.grid_index-self.cols]
                    print(f"top child: {child_cell.grid_index}")
                if d=="right" and not curr_cell.walls["right"] and curr_cell.grid_index<len(self.grid)-1:
                    child_cell=self.grid[curr_cell.grid_index+1]
                    print(f"right child: {child_cell.grid_index}")
                if not child_cell or child_cell in explored:
                    continue
                explored.add(child_cell)
                frontier.append(child_cell)
        












            






        



            



    


            


                    
                
            
                




        


            

        




            
            




   


    



    