"button.py features a Button class representing a game button."
import pygame
pygame.init()

class Button:
    "A Button object"
    def __init__(self, window:pygame.Surface, width=50, height=50, font_size=12, text="Button object", coords=(0,0), color=(0,0,0), hover_color=(255, 255, 255), 
                 text_color=(255, 255, 255)):
        """Initializes the button.
        window : the game window on which the button is displayed,
        width: the width of the button (50px by default),
        height : the height of the button (50px by default),
        font_size the size of the text font (12px by default),
        text : the text displayed on the button,
        coords : x and y coordinates of the button on the window, tuple (x, y),
        color : the color of the button (RGB, tuple),
        hover_color : the color displayed on the borders of the button when hovered by the mouse (RGB, tuple),
        text_color : the color of the text (RGB, tuple)"""

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
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False

        # Initialize the button's rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def draw(self):
        """Draws the button on the window."""

        # If the button is hovered by the mouse
        if self.is_hovered:
            # Display the hover color around the button
            hover_rect = pygame.Rect(self.rect.x - 2, self.rect.y - 2,
                                     self.width + 4, self.rect.height + 4)
            
            pygame.draw.rect(self.window, self.hover_color, hover_rect)


        # Draw the button
        pygame.draw.rect(self.window, self.color, self.rect)

        # Display the text
        text_surf = self.font.render(self.text, True, self.text_color)
        # Center the text
        text_rect = text_surf.get_rect(center=self.rect.center)

        self.window.blit(text_surf, text_rect)

    def update(self, mouse_pos:tuple):
        "Update the button's hovering state based on the mouse position."

        # Check if the mouse is over the button
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def change_color(self, new_color=(0,0,0)):
        """Change the current color of the button for the specified new color.
        - new_color : the new color of the button (RGB, tuple)."""

        # Change the color of the button
        self.color = new_color    

    def is_clicked(self, event):
        "Check if the button was clicked, returns a boolean."
        return self.is_hovered and event.type == pygame.MOUSEBUTTONDOWN and event.button in [1,2,3]            
