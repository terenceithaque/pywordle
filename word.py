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


def letter_positions(word:str|list[str]) -> dict:
    """Returns a dict containining the different positions of all letters in the given word.
    word: a string or a list of single characters."""

    positions = {}

    for i in range(len(word)):
        letter = word[i]
        if letter in positions.keys():
            positions[letter].append(i)

        else:
            positions[letter] = [i]

    return positions


def common_letter_positions(word_1:str|list[str], word_2:str|list[str]) -> dict:
    """Returns a dict containing common positions of letters by comparing the two given words.
    word_1: the first word (string, or list of single caracters),
    word_2: the second word (string, or list of single caracters)."""

    common_positions = {}

    for i, letter in enumerate(word_1):
        if word_2[i] == letter:
            if letter in common_positions.keys():
                common_positions[letter].append(i)

            else:
                common_positions[letter] = [i]

    return common_positions            



def compare_words(guess, target):
    """Compare the guess word and the target word, returns a list of statuses for each letter (placed, misplaced, not in word)."""

    status = [""] * len(guess)
    # List the letters of the guess and the target word
    target_letters = list(target)
    guess_letters = list(guess)

    for i in range(len(guess_letters)):
        # If the letter is well placed
        if guess_letters[i] == target_letters[i]:
            status[i] = "placed"
            target_letters[i] = None
            guess_letters[i] = None


    for i in range(len(guess_letters)):
        if guess_letters[i] is not None:
            # If the letter is misplaced
            if guess_letters[i] in target_letters:
                status[i] = "misplaced"
                target_letters[target_letters.index(guess_letters[i])] = None

            # If the letter is not in the target word
            else:
                status[i] = "not_in_word"

    return status                                        




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

    def add(self, letter:str, row=0, column=0) -> None:
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

    def free_columns_in_row(self, row=0) -> list[tuple]:
        """Returns a list of tuples with the positions (row, column) of all free columns in the given row.
        - row: the row in which to find free columns, int (0 by default)."""

        # Assertions
        assert row <= self.n_rows and row >= 0, f"The row number must be comprised between 0 and {self.n_rows} included."

        # Get the content of the row
        row_content = self.content[row]

        # We consider free columns as those with an empty string as content
        free_columns = [i for i in range(len(row_content)) if row_content[i] == ""]

        return [(row, column) for column in free_columns]
    
    def cartesian_coords(self, row=0, column=0) -> tuple:
        """Returns the cartesian (x, y) coordinates of the cell located at (row, column).
        row: the row in which the cell is located.
        column: the column in which the cell is located."""

        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows} included."
        assert column >= 0 and column <= self.n_columns, f"The column number must be comprised between 0 and {self.n_columns} included."

        spacing = 5

        cell_x = self.x + column * (self.square_width + spacing)
        cell_y = self.y + row * (self.square_height + spacing)

        return (cell_x, cell_y)
    
    def delete_letter(self, row=0, column=0) -> None:
        """Delete the letter in the cell located at position (row, column).
        - row: the row in which the cell is located,
        - column: the column in which the cell is located."""

        # Assertions
        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows}."
        assert column >= 0 and column <= self.n_columns, f"The column number must be comprised between 0 and {self.n_columns}"

        self.content[row][column] = ""


    def delete_word(self, row=0) -> None:
        """Delete the word contained in the given row in the grid.
        -row: the row in which the word is located."""

        # Assertions
        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows}."

        word = self.content[row]
        for i in range(len(word)):
            word[i] = ""    


    def get_word(self, row=0) -> list[str]:
        """Returns the word contained in the specified row.
        row: the number of the row where the word is located"""

        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows}"

        return self.content[row]
    

    def misplaced_letters(self, row=0, word="") -> list:
        """Compares the position of letters in the given row with the ones of the given word, and return a list of misplaced letters."""

        # Assertions
        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows}."

        # List of misplaced letters
        misplaced = []

        word_letters = list(word)
        row_content = self.content[row]

        print("Word length :", len(word_letters), "row length :", len(row_content))

        for i in range(len(row_content)):
            letter = row_content[i]
            if letter != word_letters[i] and letter in word_letters:
                misplaced.append(letter)

        return misplaced


    def letters_not_in_word(self, row=0, word="") -> list:
        """Returns a list of letters in the given row that aren't in the given word."""
        # Assertions
        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows}."

        # List of letters not in the given word
        not_in_word = []

        word_letters = list(word)
        row_content = self.content[row]

        for i in range(len(row_content)):
            letter = row_content[i]
            if letter not in word_letters:
                not_in_word.append(letter)

        return not_in_word




    def draw_cell(self, row=0, column=0, cell_color=(0,0,0)) -> None:
        """Draw a specific cell located at the position (row, column) of the WordGrid using the given color.
        -row: the row in which the cell is located,
        -column: the column in which the cell is located,
        -cell_color: the color used to fill the cell."""

        # Assertions
        assert row >= 0 and row <= self.n_rows, f"The row number must be comprised between 0 and {self.n_rows}."
        assert column >= 0 and column <= self.n_columns, f"The column number must be comprised between 0 and {self.n_columns}."

        # Get the letter inside of the cell
        letter = self.content[row][column]

        # Convert the cell's row and column to cartesian coordinates
        coords = self.cartesian_coords(row, column)
        x = coords[0]
        y = coords[1]

        # Draw a rectangle representing the cell
        pygame.draw.rect(self.window, cell_color, (x, y, self.square_width, self.square_height))
        # Display the text inside of the rectangle
        text_font = pygame.font.Font(None, self.font_size)
        text_display = text_font.render(letter, True, self.text_color)
        self.window.blit(text_display, (x,y))

        




    
    def draw(self) -> None:
        """Draw the WordGrid on the screen."""

        # Starting position
        x = self.x
        y = self.y

        # Loop over each row in the content of the grid
        for row in self.content:
            # For each letter in the row
            for letter in row:
                # Draw a rectangle at the current (x, y) position
                pygame.draw.rect(self.window, (0,0,0),(x, y, self.square_width, self.square_height))
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
    


        
