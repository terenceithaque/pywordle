"game.py handles the main game loop"
import pygame
pygame.init()
from tkinter import messagebox
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


        # Color code for the game
        self.color_code = {
            "placed":(0,255,0),
            "misplaced":(255,200,28),
            "not_in_word":(128,128,128)
        }

        # Running state tracking variable
        self.running = True


    def run(self) -> None:
        "Run the game loop until the game ends running."

        # Read the words file and split its content using the newline separator
        words = read_words_file().split("\n")
        print(words)

        # Choose a random word
        word = random.choice(words).upper()
        print("Chosen word :", word)

        # Test button
        """test_button = Button(self.window, width=100, height=50, font_size=24, text="Test button", coords=(50, 50), color=(0,0,0), hover_color=(128, 128, 128), 
                             text_color=(255,255,255))"""
        

        # Button to change keyboard layout
        change_layout_button = Button(self.window, 180, 50, 24, "AZERTY -> QWERTY", (0,0), (0,0,0), (255,0,0), (255,255,255))

        # AZERTY keyboard layout
        azerty = [("A","Z","E","R","T","Y","U","I","O","P"),
                    ("Q","S","D","F","G","H","J","K","L","M"),
                    ("W","X","C","V","B","N")]
        
        # QWERTY keyboard layout
        qwerty = [("Q","W","E","R","T","Y","U","I","O","P"),
                  ("A","S","D","F","G","H","J","K","L"),
                  ("Z","X","C","V","B","N","M")]
        # Game keyboard
        keyboard = KeyBoard(self.window, azerty, (50,550), (66,528), 50, 50, 24, 25, (0,0,0), (255,0,0), (255,255,255))
        keyboard.generate_buttons()
        # Add a Return button
        keyboard.add_button("<- Return", (510, 700), 300, 50, 24, (0,0,0), (255,0,0), (255,255,255))
        # Add a Del button
        keyboard.add_button("<× Del", (650, 490), 125, 50, 24, (0,0,0), (255,0,0), (255,255,255))

        # Word grid
        word_grid = WordGrid(self.window, n_rows=6, n_columns=5, square_width=50, square_height=50, font_size=24, text_color=(255,255,255), pos=(240, 120))
        #word_grid.add("A",0,0)

        print("Word grid content :", word_grid.content)
        print("Free columns in the first row :", word_grid.free_columns_in_row(0))

        # Current grid row
        current_row = 0
        # Current grid column
        current_column = 0

        misplaced_letters = []
        not_in_word = []
        
        # While the game is running
        while self.running:

            #print(list(range(current_column + 1)))

            pygame.time.wait(100)

            # Position of the mouse
            mouse_pos = pygame.mouse.get_pos()

            # Update the keyboard based on the current mouse position
            keyboard.update(mouse_pos)

            # Get pressed keys
            keys = pygame.key.get_pressed()

            

            

            #test_button.update(pygame.mouse.get_pos())
            
            self.window.fill((255, 255, 255))
            # Check for game and user events
            for event in pygame.event.get():
                # If the player wants to quit the game
                if event.type == pygame.QUIT:
                    # End running the game
                    self.running = False

                """if event.type == pygame.MOUSEMOTION:
                    print(pygame.mouse.get_pos())"""    

                if change_layout_button.is_clicked(event):
                    if change_layout_button.text == "AZERTY -> QWERTY":
                        keyboard.change_layout(qwerty)
                        keyboard.add_button("<- Return", (720, 625), 75, 130, 24, (0,0,0), (255,0,0), (255,255,255))
                        keyboard.add_button("<× Del", (650, 490), 125, 50, 24, (0,0,0), (255,0,0), (255,255,255))
                        change_layout_button.change_text("QWERTY -> AZERTY")

                    elif change_layout_button.text == "QWERTY -> AZERTY":
                        keyboard.change_layout(azerty)
                        keyboard.add_button("<- Return", (510, 700), 300, 50, 24, (0,0,0), (255,0,0), (255,255,255))
                        keyboard.add_button("<× Del", (650, 490), 125, 50, 24, (0,0,0), (255,0,0), (255,255,255))
                        change_layout_button.change_text("AZERTY -> QWERTY")

                for button in keyboard.buttons:

                    # Handle the Return button
                    if button.text == "<- Return":
                        if button.is_clicked(event):
                            print("Return button clicked.")
                            if current_column == 5 and current_row < 5:

                                # Update misplaced letters and letters not in the chosen word
                                misplaced_letters.append(word_grid.misplaced_letters(current_row, current_column))
                                not_in_word.append(word_grid.letters_not_in_word(current_row, current_column))
                                print(f"Misplaced letters compared to {word} : {misplaced_letters}")
                                print(f"Letters not in {word} : {not_in_word}")

                                # The next letters will be written in the next row beginning from the next column
                                current_row += 1
                                current_column = 0

                            else:
                                messagebox.showinfo("Too short !", "Word too short !")

                    # Handle the Del button
                    elif button.text == "<× Del":
                        if button.is_clicked(event):
                            print("Del button clicked.")


                            # Remove the last letter entered in the grid
                            if current_column > 0:
                                current_column -= 1
                                word_grid.delete_letter(current_row, current_column)
                                print("Word grid content :", word_grid.content)
                            
                                print("Current column :", current_column)             

                    # Other buttons
                    else:
                        if button.is_clicked(event):
                            # Get the button's letter and write it to the current row and column in the word grid
                            letter = button.text
                            word_grid.add(letter, current_row, current_column)
                            print("Word grid content :", word_grid.content)
                            print(f"Cartesian coords for ({current_row}, {current_column}) : {word_grid.cartesian_coords(current_row, current_column)}.")

                            # Move to the next column
                            current_column += 1

                # If a key is pressed
                if event.type == pygame.KEYDOWN:
                    
                    # Handle the Return button
                    if event.key == pygame.K_RETURN:
                        print("Return key pressed.")
                        button_text = "<- Return"
                        return_button = keyboard.find_button_by_text(button_text)
                        return_button.is_hovered = True
                        # Update the current row and column
                        if current_column == 5 and current_row < 5:
                            # Update misplaced letters and letters not in the chosen word
                            misplaced_letters.append(word_grid.misplaced_letters(current_row, word))
                            not_in_word.append(word_grid.letters_not_in_word(current_row, word))
                            print(f"Misplaced letters compared to {word} : {misplaced_letters}")
                            print(f"Letters not in {word} : {not_in_word}")
                            # The next letters will be written in the next row beginning from the next column
                            current_row += 1
                            current_column = 0

                        else:
                            messagebox.showinfo("Too short !", "Word too short !")    
                    
                    # Handle the Del button
                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        print("Del button pressed")
                        button_text = "<× Del"
                        del_button = keyboard.find_button_by_text(button_text)
                        del_button.is_hovered = True

                        # Remove the last letter entered in the grid
                        if current_column > 0:
                            current_column -= 1
                            word_grid.delete_letter(current_row, current_column)
                            print("Word grid content :", word_grid.content)
                            
                            print("Current column :", current_column)
    

                    # Handle other buttons    
                    else:
                        # Get the text of the key
                        key_text = event.unicode
                        print(f"Key text : {key_text}")

                    
                    
                        # The letter to insert is the text of the key in upper case
                        letter = key_text.upper()

                        button = keyboard.find_button_by_text(letter)
                        button.is_hovered = True

                        print("Current column :", current_column)

                        print(word_grid.get_word(current_row))
                        if any(["" in word_grid.get_word(current_row)]):
                            word_grid.add(letter, current_row, current_column)
                            print(f"Cartesian coords for ({current_row}, {current_column}) : {word_grid.cartesian_coords(current_row, current_column)}.")
                        
                        print("Word grid content :", word_grid.content)

                        # Move to the next column
                        if current_column < 5:
                            current_column += 1        





                """if test_button.is_clicked(event):
                    print("Button clicked !")

                else:
                    print("No button clicked.")"""        

            #test_button.draw()

            

            change_layout_button.update(mouse_pos)

            
            # Display the word grid
            word_grid.draw() 
            

            # Display the cells and keyboard buttons with misplaced letters or letters not in the chosen word
            for row in range(current_row):
                for column in range(len(word_grid.content[row])):
                    letter = word_grid.content[row][column]
                    for letter_row in misplaced_letters:
                        if letter in letter_row:
                            word_grid.draw_cell(row, column, self.color_code["misplaced"])
                            keyboard.set_button_color(letter, self.color_code["misplaced"])

                        else:
                            word_grid.draw_cell(row, column, self.color_code["placed"])
                            keyboard.set_button_color(letter, self.color_code["placed"])    

                    for letter_row in not_in_word:
                        if letter in letter_row:
                            word_grid.draw_cell(row, column, self.color_code["not_in_word"])
                            keyboard.set_button_color(letter, self.color_code["not_in_word"])    


            change_layout_button.draw()

            # Display the keyboard
            keyboard.draw()

            

            # Update the window
            pygame.display.flip()            
