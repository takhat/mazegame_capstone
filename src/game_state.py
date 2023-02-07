import pygame, sys
from player import Player
from constants import *


class GameState:
    """keeps track of state of the game: Start, Play, End."""
    def __init__(self, mg, canvas, sprite_group, player, cell_width):
        self.state="play_game"
        self.mg=mg
        self.grid=self.mg.grid
        self.cell_dict={}
        self.all_sprites=sprite_group
        self.player=player
        self.cell_width=cell_width
        self.canvas=canvas
        self.move_down=False
        self.move_up=False
        self.move_left=False
        self.move_right=False

        for cell in self.grid:
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
        pygame.display.flip()
        current_cell = self.cell_dict[(self.player.rect.x,self.player.rect.y)]
        if current_cell.grid_index==len(self.grid)-1:
            print("game over")
            self.state="game_over"
            self.game_over()
            
    def redraw_game_window(self):
        self.mg.draw_maze()
        self.all_sprites.draw(self.canvas)   

    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.canvas.fill((0,0,0))
        font=pygame.font.SysFont("arial", 30)
        title=font.render("Congratulations! You win!", True, (255,255,255))
        # restart_button=font.render("R: Restart", True, (255,255,255))
        quit_button=font.render("Q: Quit", True, (255,255,255))
        self.canvas.blit(title, (width//2 -title.get_width()//2, height//2 -title.get_height()//3))
        # self.canvas.blit(restart_button, (width//2 -restart_button.get_width()//2, height//1.9 -restart_button.get_height()))
        self.canvas.blit(quit_button, (width//2 - quit_button.get_width()//2, height//2 + quit_button.get_height()//2))
        pygame.display.update()

    def state_manager(self):
        if self.state=="game_over":
            self.game_over()
            keys=pygame.key.get_pressed()
            if keys[pygame.K_r]:
                print("r key pressed to restart game")
                self.state="restart_game"
            if keys[pygame.K_q]:
                print("q key pressed to quit game")
                pygame.quit()
                sys.exit()

        elif self.state=="play_game":
            self.main_game()
        
        elif self.state=="restart_game":
            self.canvas.fill((0,0,0))
            






