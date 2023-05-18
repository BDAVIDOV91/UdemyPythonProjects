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
    global grid
    grid = [list(row) for row in zip(*grid)]

# Function to reverse the grid
def reverse():
    global grid
    grid = [row[::-1] for row in grid]

# Function to compress the grid by moving tiles to the left
def compress():
    global grid
    new_grid = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][j][pos] = grid[i][j]
                pos += 1
    grid = new_grid
    
# Function to merge tiles in the grid
def merge():
    pass

# Function to update the game screen
def update_screen():
    pass

# Main game loop
def main():
    pass