import random
import curses

# Initialize the screen.
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.keypad(1)
stdscr.timeout(100)

# Set up the grid
grid = [[0 for _ in range(4)] for _ in range(4)]

# Function to add a new random title (2 or 4) to the grid
def add_title():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])
        
# Function to transpose the grid
def transpose():
    pass

# Function to reverse the grid
def reverse():
    pass
