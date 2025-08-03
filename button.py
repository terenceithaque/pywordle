"button.py features a Button class representing a game button."
import pygame
pygame.init()

class Button:
    "A Button object"
    def __init__(self, window:pygame.Surface, width=50, height=50, font_size=12, text="Button object", coords=(0,0), color=(0,0,0), on_click=None):
        """Initializes the button.
        window : the game window on which the button is displayed,
        width: the width of the button (50px by default),
        height : the height of the button (50px by default),
        font_size the size of the text font (12px by default),
        text : the text displayed on the button,
        coords : x and y coordinates of the button on the window, tuple (x, y),
        on_click : function or action triggered when the button is clicked, None by default."""

        # Initialize the button's attributes
        self.window = window
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.coords = coords
        self.x = self.coords[0]
        self.y = self.coords[1]
        self.color = color
        self.on_click = on_click

        # Initialize the button's rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def draw(self):
        """Draws the button on the window."""    
