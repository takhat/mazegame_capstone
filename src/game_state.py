import pygame, sys

# pygame.init()
class GameState:
    """keeps track of state of the game: Start, Play, End."""
    def __init__(self):
        self.state="main_game"
    def main_game(self):
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
            pygame.display.flip()   #displayes anything that's drawn inside the while loop
                
    