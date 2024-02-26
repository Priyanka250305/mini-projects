# Define the size of the grid
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Create an empty grid
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Define the initial state of the grid
initial_state = [
    (3, 1), (1, 2), (2, 1), (2, 3), (3, 2)  # Example initial state
]

# Set the initial state on the grid
for x, y in initial_state:
    grid[y][x] = 1

# Function to count the number of live neighbors for a given cell
def count_live_neighbors(x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                count += grid[ny][nx]
    return count

# Function to update the grid for the next generation
def update_grid():
    new_grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            live_neighbors = count_live_neighbors(x, y)
            if grid[y][x] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = 1
            else:
                if live_neighbors == 3:
                    new_grid[y][x] = 1
    return new_grid

# Function to print the grid
def print_grid():
    for row in grid:
        for cell in row:
            print('X' if cell == 1 else '.', end=' ')
        print()

# Run the game for a certain number of generations
num_generations = 2
for generation in range(num_generations):
    print(f'Generation {generation + 1}:')
    print_grid()
    grid = update_grid()
    print()