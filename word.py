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
    def __init__(self, window:pygame.Surface, n_rows=5, n_columns=5):
        """Initializes the WordGrid."""

        # Initialize attributes
        self.window = window
        self.n_rows = n_rows
        self.n_columns = n_columns

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

        
