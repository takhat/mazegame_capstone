import pygame, sys

from player import Player

# pygame.init()
class GameState:
    """keeps track of state of the game: Start, Play, End."""
    def __init__(self, canvas, grid, sprite_group, player, cell_width):
        self.state="main_game"
        self.grid=grid
        self.sprite_group=sprite_group
        self.player=player
        self.velocity=cell_width
        self.canvas=canvas

    def main_game(self):
        self.grid.draw_maze()
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print("left key pressed")
            self.player.set_position(self.player.rect.x-self.velocity,self.player.rect.y)
            pygame.display.update()
        elif keys[pygame.K_RIGHT]:
            print("right key pressed")
            self.player.set_position(self.player.rect.x+self.velocity,self.player.rect.y)
            pygame.display.update()

        # pygame.display.flip()   #displayes anything that's drawn inside the while loop
                
    def redraw_game_window(self, x, y):
        self.grid.draw_maze()
        self.player.set_position(x, y)
        self.sprite_group.draw(self.canvas)               
        pygame.display.update()