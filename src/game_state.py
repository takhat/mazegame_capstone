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
        self.start_screen=True
        self.display_solution=False
        self.level=1

    def create_new_game(self):
        """initializes a new maze and sprite and displays it on canvas."""
        # initalize Pygame
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(f'Welcome to the maze game! Level {self.level}')
        
        self.width = (cell_width*rows*self.level)+(2*cell_width) 
        self.height = (cell_width*rows*self.level)+(2*cell_width)
        self.canvas=pygame.display.set_mode((self.width, self.height))

        #Maze 
        mg = MazeGenerator(canvas=self.canvas,rows=rows, cols=cols, cell_width=cell_width, level=self.level)
        mg.create_grid() 
        mg.generate_maze()
        mg.draw_maze()

        #Sprite/Player 
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.player.set_position(mg.grid[0].x, mg.grid[0].y)
        self.all_sprites.draw(self.canvas) 
        self.mg=mg
        self.grid=mg.grid
        for cell in self.grid:
            self.cell_dict[(cell.x, cell.y)]=cell
    
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
                if event.key == pygame.K_h:
                    self.mg.draw_solution(self.level*rows*cell_width, self.level*rows*cell_width)
                    self.display_solution=True
                
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
                self.player.set_position(x+cell_width, y)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_left:
            print("left key pressed")
            if current_cell.walls["left"] or current_cell.grid_index==0:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x-cell_width, self.player.rect.y)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_up:
            print("up key pressed")
            if current_cell.walls["top"]:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x, self.player.rect.y-cell_width)
                print(self.player.rect.x, self.player.rect.y)
                print(f"grid_index:{self.cell_dict[(self.player.rect.x,self.player.rect.y)].grid_index}")
                self.redraw_game_window()

        if self.move_down:
            print("down key pressed")
            if current_cell.walls["bottom"]:
                print("movement not allowed")
            else:
                self.player.set_position(self.player.rect.x, self.player.rect.y+cell_width)
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
        font=pygame.font.SysFont("arial", 18)
        title=font.render(f"Congratulations! You won Level {self.level}!", True, (255,255,255))
        restart_button=font.render("N: Next Level", True, (255,255,255))
        quit_button=font.render("Q: Quit", True, (255,255,255))
        self.canvas.blit(title, (self.width//2 - title.get_width()//2, self.height//2 - title.get_height()*2))
        if self.level<3:
            self.canvas.blit(restart_button, (self.width//2 -restart_button.get_width()//2, self.height//1.5 -restart_button.get_height()))
        self.canvas.blit(quit_button, (self.width//2 - quit_button.get_width()//2, self.height//2 + quit_button.get_height()//2))
        pygame.display.update()


    def state_manager(self):
        """allows functionality based on game state."""
        if self.state=="game_over":
            self.game_over()
            keys=pygame.key.get_pressed()
            if keys[pygame.K_n] and self.level<3:
                print("n key pressed to generate next level game")
                self.state="new_game"
            if keys[pygame.K_q]:
                print("q key pressed to quit game")
                pygame.quit()
                sys.exit()

        elif self.state=="play_game":
            self.main_game()
        
        elif self.state=="new_game":
            self.canvas.fill((0,0,0))
            self.state="play_game"
            self.cell_dict={}
            self.move_down=False
            self.move_up=False
            self.move_left=False
            self.move_right=False
            self.new_game=True
            self.level+=1
            self.state="play_game"
            self.display_solution=False
        






        
            
            
            







