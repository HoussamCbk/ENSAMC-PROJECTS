import pyfiglet
import random
import time
import os

def clear_screen():
    # Function to clear the screen in cmd
    os.system('cls' if os.name == 'nt' else 'clear')

def happy_birthday():
    colors = ['blue', 'green', 'white']  # Restrict to blue and green
    ascii_art = pyfiglet.figlet_format("Happy Birthday, Khoya", font="slant")
    
    color_codes = {
        'blue': 34,  # ANSI code for blue
        'green': 32,  # ANSI code for green
        'white' : 37 # ANSI code for cyan 
    }
    
    while True:
        for color in colors:
            clear_screen()
            print(f"\033[{color_codes[color]}m{ascii_art}\033[0m")  # Apply color
            time.sleep(0.5)

happy_birthday()
