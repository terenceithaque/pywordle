"main.py is the entry point for the application."
import pygame
pygame.init()
from game import *
from tkinter import messagebox


window_width = 800
window_height = 800

# Run the game a first time
game = Application(window_width, window_height)
game.run()
pygame.quit()


# Ask the player if he wants to replay or not
replay = messagebox.askyesno("Replay ?", "Do you want to replay ?")

# While the player answers "yes"
while replay:
    # Re-init pygame
    pygame.init()

    # Launch the game
    game = Application(window_width, window_height)
    game.run()

    # Quit pygame
    pygame.quit()

    # Re-ask the player
    replay = messagebox.askyesno("Replay ?", "Do you want to replay ?")
