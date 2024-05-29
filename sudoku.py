def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_safe(grid, row, col, num):
    # Check if 'num' is not present in the current row, column, and the 3x3 grid
    return (
        all(num != grid[row][j] for j in range(9)) and
        all(num != grid[i][col] for i in range(9)) and
        all(num != grid[i][j] for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3))
    )

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def solve_sudoku(grid):
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True  # If no empty location is found, the puzzle is solved
    row, col = empty_loc

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True 

            grid[row][col] = 0 

    return False 

# Example usage:
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_grid):
    print("Sudoku Solved:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
