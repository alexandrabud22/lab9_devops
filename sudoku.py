def readFile():
    with open("sudoku.txt", "r") as f:
        grid = [[int(num) for num in line.strip()] for line in f]
    return grid

def valid(grid, row, col, n):
    for i in range(9):
        if grid[row][i] == n or grid[i][col] == n:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[startRow + i][startCol + j] == n:
                return False
    return True

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for n in range(1, 10):
                    if valid(grid, row, col, n):
                        grid[row][col] = n
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def solve_sudoku(grid):
    import copy
    if not isinstance(grid, list) or len(grid) != 9 or any(len(row) != 9 for row in grid):
        raise ValueError("Input must be a 9x9 grid.")
    board = copy.deepcopy(grid)
    return board if solve(board) else None
