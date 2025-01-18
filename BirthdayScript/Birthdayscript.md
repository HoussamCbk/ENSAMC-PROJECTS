# Happy Birthday Script

This Python script creates a dynamic and colorful "Happy Birthday" message using ASCII art. It alternates between blue, green, and white colors in a blinking effect for a celebratory display.

## Features

- Displays "Happy Birthday" in large ASCII art using the `pyfiglet` library.
- Alternates text colors (for example : blue, green, and white) for a blinking effect.
- Runs in an infinite loop to continuously display the message.
- Includes a clear screen function to keep the terminal output clean.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
  
  Install Python [here](https://www.python.org/downloads/).
  
- The `pyfiglet` library
  
  Copy this command to the cmd
  
  ```
  pip install pyfiglet
  ```
  or use this command

  ```
  pip3 install pyfiglet
  ```
  
- The `termcolor` library

   Copy this command to the cmd
  
    ```
    pip install termcolor
    ```
    or use this command
  
    ```
    pip3 install termcolor
    ```

  

## The working theory

1. **Color Codes**: The script uses ANSI color codes for text formatting in the terminal:
   - **Blue**: `34`
   - **Green**: `32`
   - **White**: `37`
  
    Here's a table of ANSI color codes if you want to add or choose your own colors :

   ### Regular Colors

    | Value    | Color  |
    | -------- | ------ |
    | \e[0;30m | Black  |
    | \e[0;31m | Red    |
    | \e[0;32m | Green  |
    | \e[0;33m | Yellow |
    | \e[0;34m | Blue   |
    | \e[0;35m | Purple |
    | \e[0;36m | Cyan   |
    | \e[0;37m | White  |

   ### Bold

    | Value    | Color  |
    | -------- | ------ |
    | \e[1;30m | Black  |
    | \e[1;31m | Red    |
    | \e[1;32m | Green  |
    | \e[1;33m | Yellow |
    | \e[1;34m | Blue   |
    | \e[1;35m | Purple |
    | \e[1;36m | Cyan   |
    | \e[1;37m | White  |

   ### Underline

    | Value    | Color  |
    | -------- | ------ |
    | \e[4;30m | Black  |
    | \e[4;31m | Red    |
    | \e[4;32m | Green  |
    | \e[4;33m | Yellow |
    | \e[4;34m | Blue   |
    | \e[4;35m | Purple |
    | \e[4;36m | Cyan   |
    | \e[4;37m | White  |

   ### Background

    | Value  | Color  |
    | ------ | ------ |
    | \e[40m | Black  |
    | \e[41m | Red    |
    | \e[42m | Green  |
    | \e[43m | Yellow |
    | \e[44m | Blue   |
    | \e[45m | Purple |
    | \e[46m | Cyan   |
    | \e[47m | White  |

   ### High Intensity

    | Value    | Color  |
    | -------- | ------ |
    | \e[0;90m | Black  |
    | \e[0;91m | Red    |
    | \e[0;92m | Green  |
    | \e[0;93m | Yellow |
    | \e[0;94m | Blue   |
    | \e[0;95m | Purple |
    | \e[0;96m | Cyan   |
    | \e[0;97m | White  |

   ### Bold High Intensity

    | Value    | Color  |
    | -------- | ------ |
    | \e[1;90m | Black  |
    | \e[1;91m | Red    |
    | \e[1;92m | Green  |
    | \e[1;93m | Yellow |
    | \e[1;94m | Blue   |
    | \e[1;95m | Purple |
    | \e[1;96m | Cyan   |
    | \e[1;97m | White  |

   ### High Intensity backgrounds

    | Value     | Color  |
    | --------- | ------ |
    | \e[0;100m | Black  |
    | \e[0;101m | Red    |
    | \e[0;102m | Green  |
    | \e[0;103m | Yellow |
    | \e[0;104m | Blue   |
    | \e[0;105m | Purple |
    | \e[0;106m | Cyan   |
    | \e[0;107m | White  |


3. **Infinite Loop**: A `while` loop ensures the display continues until manually terminated (e.g., by pressing `Ctrl+C`).

4. **Clear Screen**: The `clear_screen()` function clears the terminal output to create a clean transition between color changes.

5. **Dynamic Coloring**: The script cycles through the specified colors (`blue`, `green`, and `white`) to create the blinking effect.

## Code

```python
import pyfiglet
import random
import time
import os

def clear_screen():
    # Function to clear the screen in cmd
    os.system('cls' if os.name == 'nt' else 'clear')

def happy_birthday():
    colors = ['blue', 'green', 'white']  # Restrict to blue, green, and white
    ascii_art = pyfiglet.figlet_format("Happy Birthday", font="slant")
    
    color_codes = {
        'blue': 34,  # ANSI code for blue
        'green': 32,  # ANSI code for green
        'white': 37   # ANSI code for white
    }
    
    while True:
        for color in colors:
            clear_screen()
            print(f"\033[{color_codes[color]}m{ascii_art}\033[0m")  # Apply color
            time.sleep(0.5)

happy_birthday()
```

### **Made by Choubik Houssam :smiley:**

