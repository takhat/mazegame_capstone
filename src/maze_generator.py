from cell import Cell

class MazeGenerator:
    """helps to create and position cells inside a grid, and generate and draw a maze from the grid."""
    def __init__(self, canvas, rows, cols, cell_width, level):
        self.canvas=canvas
        self.level=level
        self.rows=rows*level
        self.cols=cols*level
        self.cell_width=cell_width
        self.grid=[]
        # self.visited=[]
        self.stack=[]

    
    def create_grid(self):
        """makes cells and positions them in a 1D list called grid."""
        index=0
        for row in range(self.rows):
            for col in range(self.cols):
                cell = Cell(grid_index=index,row_index=row, col_index=col, cell_width=self.cell_width,canvas=self.canvas, level=self.level)
                self.grid.append(cell)
                index+=1
        
    def generate_maze(self):
        """generates a maze using randomized depth first search (Randomized DFS)."""
        # Choose the initial cell, mark it as visited and push it to the stack
        initial = self.grid[0]
        initial.visited=True
        # self.visited.append(initial)
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
                # self.visited.append(chosen)
                self.stack.append(chosen)
        
    def draw_maze(self):  
        """draws the maze."""
        for cell in self.grid:
            cell.draw(self.canvas)


    