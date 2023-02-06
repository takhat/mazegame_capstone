import pygame, sys

from player import Player

# pygame.init()
class GameState:
    """keeps track of state of the game: Start, Play, End."""
    def __init__(self, canvas, mg, sprite_group, player, cell_width, move_down, move_up, move_left, move_right):
        self.state="main_game"
        self.mg=mg
        self.grid=self.mg.grid
        self.cell_dict={}
        self.all_sprites=sprite_group
        self.player=player
        self.cell_width=cell_width
        self.canvas=canvas
        self.move_down=move_down
        self.move_up=move_up
        self.move_left=move_left
        self.move_right=move_right

        for cell in mg.grid:
            self.cell_dict[(cell.x, cell.y)]=cell
        
    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.move_right=True
                if event.key == pygame.K_LEFT:
                    self.move_left=True
                if event.key == pygame.K_UP:
                    self.move_up=True
                if event.key == pygame.K_DOWN:
                    self.move_down=True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.move_right=False
                if event.key == pygame.K_LEFT:
                    self.move_left=False
                if event.key == pygame.K_UP:
                    self.move_up=False
                if event.key == pygame.K_DOWN:
                    self.move_down=False
        x=self.player.rect.x
        y=self.player.rect.y
        current_cell = self.cell_dict[(x,y)]
        if self.move_right:
            print("right key pressed")
            if current_cell.walls["right"] or current_cell.grid_index==len(self.grid)-1:
                print("movement not allowed")
            else:
                self.player.set_position(x+self.cell_width, y)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_left:
            print("left key pressed")
            if current_cell.walls["left"] or current_cell.grid_index==0:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x-self.cell_width, self.player.rect.y)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_up:
            print("up key pressed")
            if current_cell.walls["top"]:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x, self.player.rect.y-self.cell_width)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_down:
            print("down key pressed")
            if current_cell.walls["bottom"]:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x, self.player.rect.y+self.cell_width)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()
        current_cell = self.cell_dict[(self.player.rect.x,self.player.rect.y)]
        # if current_cell.grid_index==len(grid)-1:
        #     print("Congrats!")
        pygame.display.flip()
    
    def redraw_game_window(self):
        self.mg.draw_maze()
        self.all_sprites.draw(self.canvas)           