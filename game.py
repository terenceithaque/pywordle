"game.py handles the main game loop"
import pygame
pygame.init()
import random
from word import *

class Application():
    """An instance of the game."""
    def __init__(self, window_width=800, window_height = 600) -> None:
        """Setup the application instance and window.
        window_width : the width of the current game window, by default 500px,
        window_height: the height of the current game window, by default 600px."""

        # Window dimensions
        self.window_width = window_width
        self.window_height = window_height

        # Set up the window
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # Running state tracking variable
        self.running = True


    def run(self) -> None:
        "Run the game loop until the game ends running."

        # Read the words file and split its content using the newline separator
        words = read_words_file().split("\n")
        print(words)

        # Choose a random word
        word = random.choice(words)
        print("Chosen word :", word)

        # While the game is running
        while self.running:

            # Check for game and user events
            for event in pygame.event.get():
                # If the player wants to quit the game
                if event.type == pygame.QUIT:
                    # End running the game
                    self.running = False


            # Update the window
            pygame.display.flip()            
