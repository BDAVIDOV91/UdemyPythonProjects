import random
import curses

# Initialize the screen.
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.keypad(1)
stdscr.timeout(100)

# Set up the grid
grid = [[0 for _ in range(4)] for _ in range(4)]

# Function to add a new random tile (2 or 4) to the grid
def add_tile():
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
                new_grid[i][pos] = grid[i][j]
                pos += 1
    grid = new_grid

# Function to merge tiles in the grid
def merge():
    global grid
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j + 1] = 0

# Function to update the game screen
def update_screen():
    stdscr.erase()
    stdscr.addstr("2048\n\n")
    for row in grid:
        stdscr.addstr(' '.join(str(cell) if cell != 0 else '-' for cell in row) + '\n')
    stdscr.refresh()

# Main game loop
def main():
    # Initialize the grid with one tile
    add_tile()

    while True:
        update_screen()

        # Get user input
        key = stdscr.getch()

        if key == curses.KEY_UP:
            transpose()
            compress()
            merge()
            compress()
            transpose()
        elif key == curses.KEY_DOWN:
            transpose()
            reverse()
            compress()
            merge()
            compress()
            reverse()
            transpose()
        elif key == curses.KEY_LEFT:
            compress()
            merge()
            compress()
        elif key == curses.KEY_RIGHT:
            reverse()
            compress()
            merge()
            compress()
            reverse()

        # Check if the game is over
        game_over = all(grid[i][j] != 0 for i in range(4) for j in range(4))
        if game_over:
            stdscr.addstr("\nGame Over!")
            stdscr.refresh()
            break

    # Clean up the curses
    curses.endwin()

# Add initial tile before the game loop starts
add_tile()

# Run the game
if __name__ == '__main__':
    main()