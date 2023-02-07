import pygame, sys
from maze_generator import MazeGenerator
from player import Player
from constants import *


class GameState:
    """keeps track of state of the game: Play, End, Replay."""
    def __init__(self):
        self.state="play_game"
        self.cell_dict={}
        self.move_down=False
        self.move_up=False
        self.move_left=False
        self.move_right=False
        self.new_game=True

    def create_new_game(self):
        """initializes a new maze and sprite and displays it on canvas."""
        # initalize Pygame
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Welcome to the maze game!')
        
        #Maze 
        mg = MazeGenerator(canvas=CANVAS,rows=ROWS, cols=COLS, cell_width=CELL_WIDTH)
        mg.create_grid() 
        mg.generate_maze()
        mg.draw_maze()

        #Sprite/Player 
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.player.set_position(mg.grid[0].x, mg.grid[0].y)
        self.all_sprites.draw(CANVAS) 
        self.mg=mg
        self.grid=mg.grid
        for cell in self.grid:
            self.cell_dict[(cell.x, cell.y)]=cell
        self.canvas=CANVAS

    def main_game(self):
        """provides game playing functionality. Allows to navigate maze using arrow keys."""
        if self.new_game:
            self.create_new_game()
            self.new_game=False
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
                self.player.set_position(x+CELL_WIDTH, y)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_left:
            print("left key pressed")
            if current_cell.walls["left"] or current_cell.grid_index==0:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x-CELL_WIDTH, self.player.rect.y)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_up:
            print("up key pressed")
            if current_cell.walls["top"]:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x, self.player.rect.y-CELL_WIDTH)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_down:
            print("down key pressed")
            if current_cell.walls["bottom"]:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x, self.player.rect.y+CELL_WIDTH)
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
        """helper method to display the maze and the sprite on canvas."""
        self.mg.draw_maze()
        self.all_sprites.draw(self.canvas)    

    def game_over(self):
        """displays end-game screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.canvas.fill((0,0,0))
        font=pygame.font.SysFont("arial", 30)
        title=font.render("Congratulations! You win!", True, (255,255,255))
        restart_button=font.render("R: Restart", True, (255,255,255))
        quit_button=font.render("Q: Quit", True, (255,255,255))
        self.canvas.blit(title, (width//2 - title.get_width()//2, height//2 - title.get_height()*2))
        self.canvas.blit(restart_button, (width//2 -restart_button.get_width()//2, height//1.9 -restart_button.get_height()))
        self.canvas.blit(quit_button, (width//2 - quit_button.get_width()//2, height//2 + quit_button.get_height()//2))
        pygame.display.update()

    def state_manager(self):
        """allows functionality based on game state."""
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
            self.state="play_game"
            self.cell_dict={}
            self.move_down=False
            self.move_up=False
            self.move_left=False
            self.move_right=False
            self.new_game=True
            self.state="play_game"







