from cell import Cell

class MazeGenerator:
    def __init__(self, win, grid, rows, cols, cell_width):
        if not grid:
            self.grid=[]
        self.win=win
        self.rows=rows
        self.cols=cols
        self.cell_width=cell_width
    
    def create_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = Cell(i, j, self.cell_width)
                print(i, j)
                self.grid.append(cell)

    def draw_grid(self):
        for cell in self.grid:
            cell.draw(self.win)