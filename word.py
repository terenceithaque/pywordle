"word.py allows choosing a random word from the word list file."
import random
import os

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
