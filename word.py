"word.py allows choosing a random word from the word list file."
import random
import os
import pygame

def read_words_file():
    "Reads the content of word.txt, in the script's folder."

    # Get the script's folder
    current_folder = os.path.abspath(os.path.dirname(__file__))

    # Construct the path to the .txt file
    file_path = os.path.join(current_folder, "words.txt")

    try:
        f = open(file_path, "r")
        content = f.read()
        f.close()
        return content
    
    except Exception as e:
        print(f"Error while reading the file: {e}")



class WordGrid:
    """A WordGrid object representing a word grid."""
    def __init__(self, window:pygame.Surface, n_rows=5, n_columns=5, square_width=50, square_height=50, font_size=24,text_color=(255,255,255), pos=(50,50)):
        """Initializes the WordGrid."""

        # Initialize attributes
        self.window = window
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.square_width = square_width
        self.square_height = square_height
        self.font_size = font_size
        self.text_color = text_color
        self.x = pos[0]
        self.y = pos[1]

        # Grid content
        self.content = [["" for i in range(self.n_columns)] for n in range(self.n_rows)]

    def add(self, letter:str, row=0, column=0):
        """Add the given letter at the position (row, column).
        - letter: the letter to be added in the grid, str.
        - row: row in which the letter will be inserted, int (0 by default),
        - column : column in which the letter will be inserted, int (0 by default)."""

        # Assertions
        assert row <= self.n_rows and row >= 0, f"The row number must be comprised between 0 and {self.n_rows} included."
        assert column <= self.n_columns and column >= 0, f"The column number must be comprised between 0 and {self.n_columns} included."
        assert isinstance(letter, str), "The given letter must be a string type."
        assert len(letter) == 1, "The string representing the letter must be only 1 in length."

        # Update the grid content
        self.content[row][column] = letter

    def free_columns_in_row(self, row=0):
        """Returns a list of tuples with the positions (row, column) of all free columns in the given row.
        - row: the row in which to find free columns, int (0 by default)."""

        # Assertions
        assert row <= self.n_rows and row >= 0, f"The row number must be comprised between 0 and {self.n_rows} included."

        # Get the content of the row
        row_content = self.content[row]

        # We consider free columns as those with an empty string as content
        free_columns = [i for i in range(len(row_content)) if row_content[i] == ""]

        return [(row, column) for column in free_columns]
    
    def cartesian_coords(self, row=0, column=0):
        """Returns the cartesian (x, y) coordinates of the cell located at (row, column).
        row: the row in which the cell is located.
        column: the column in which the cell is located."""

        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows} included."
        assert column >= 0 and column <= self.n_columns, f"The column number must be comprised between 0 and {self.n_columns} included."

        spacing = 5

        cell_x = self.x + column * (self.square_width + spacing)
        cell_y = self.y + row * (self.square_height + spacing)

        return (cell_x, cell_y)
    
    def delete_letter(self, row=0, column=0):
        """Delete the letter in the cell located at position (row, column).
        - row: the row in which the cell is located,
        - column: the column in which the cell is located."""

        # Assertions
        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows}."
        assert column >= 0 and column <= self.n_columns, f"The column number must be comprised between 0 and {self.n_columns}"

        self.content[row][column] = ""


    def get_word(self, row=0):
        """Returns the word contained in the specified row.
        row: the number of the row where the word is located"""

        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows}"

        return self.content[row]
    
    def draw(self):
        """Draw the WordGrid on the screen."""

        # Starting position
        x = self.x
        y = self.y

        # Loop over each row in the content of the grid
        for row in self.content:
            # For each letter in the row
            for letter in row:
                # Draw a rectangle at the current (x, y) position
                pygame.draw.rect(self.window, (125,125,125),(x, y, self.square_width, self.square_height))
                # Display the letter inside of the rectangle
                text_font = pygame.font.Font(None, self.font_size)
                text_display = text_font.render(letter, True, self.text_color)
                self.window.blit(text_display, (x,y))
                # Update the x coordinate by adding square width + an additionnal space of 5px
                x += self.square_width + 5

            # Update the y coordinate by adding square height + an additionnal space of 5px
            y += self.square_height + 5

            # Reset the x coordinate
            x = self.x    
    


        
