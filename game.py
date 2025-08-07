"game.py handles the main game loop"
import pygame
pygame.init()
import random
from word import *
from button import *

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
        pygame.display.set_caption("Terenceithaque's pywordle")

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

        # Test button
        """test_button = Button(self.window, width=100, height=50, font_size=24, text="Test button", coords=(50, 50), color=(0,0,0), hover_color=(128, 128, 128), 
                             text_color=(255,255,255))"""
        

        # Button to change keyboard layout
        change_layout_button = Button(self.window, 50, 50, 24, "AZERTY", (0,0), (0,0,0), (255,0,0), (255,255,255))

        # AZERTY keyboard layout
        azerty = [("A","Z","E","R","T","Y","U","I","O","P"),
                    ("Q","S","D","F","G","H","J","K","L","M"),
                    ("W","X","C","V","B","N")]
        
        # QWERTY keyboard layout
        qwerty = [("Q","W","R","T","Y","U","I","O","P"),
                                ("A","S","D","F","G","H","J","K","L"),
                                ("Z","X","C","V","B","N","M")]
        # Game keyboard
        keyboard = KeyBoard(self.window, azerty, (50,380), (66,238), 50, 50, 24, 25, (0,0,0), (255,0,0), (255,255,255))
        keyboard.generate_buttons()

        keyboard.change_layout([("Q","W","R","T","Y","U","I","O","P"),
                                ("A","S","D","F","G","H","J","K","L"),
                                ("Z","X","C","V","B","N","M")])
        
        # While the game is running
        while self.running:

            # Position of the mouse
            mouse_pos = pygame.mouse.get_pos()

            #test_button.update(pygame.mouse.get_pos())
            
            self.window.fill((255, 255, 255))
            # Check for game and user events
            for event in pygame.event.get():
                # If the player wants to quit the game
                if event.type == pygame.QUIT:
                    # End running the game
                    self.running = False

                if event.type == pygame.MOUSEMOTION:
                    print(pygame.mouse.get_pos())    


                """if test_button.is_clicked(event):
                    print("Button clicked !")

                else:
                    print("No button clicked.")"""        

            #test_button.draw()

            change_layout_button.update()

            # Update the keyboard based on the current mouse position
            keyboard.update(mouse_pos)

            change_layout_button.draw()

            # Display the keyboard
            keyboard.draw()

            # Update the window
            pygame.display.flip()            
