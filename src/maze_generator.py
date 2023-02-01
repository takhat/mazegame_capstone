from cell import Cell

class MazeGenerator:
    def __init__(self, win, grid, rows, cols, cell_width):
        if not grid:
            self.grid={}
        self.win=win
        self.rows=rows
        self.cols=cols
        self.cell_width=cell_width
    
    def create_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = Cell(i, j, self.cell_width)
                print(i, j)
                self.grid[(i, j)] = cell
        self.curr_cell=self.grid[(0, 0)]
    
    def draw_grid(self):
        self.curr_cell.visited=True
        next=self.curr_cell.check_neighbors(grid=self.grid)
        if next:
            next.visited=True
            self.curr_cell=next

        for cell in self.grid.values():
            cell.draw(self.win)


    