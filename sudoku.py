def find_next_empty(board):
    # find the next empty cell
    for r in range(9):  # checking rows
        for c in range(9):  # checking columns
            if board[r][c] == 0:  # 0 designates empty cell
                return r, c
    return None, None  # all cells are filled in


def is_valid(row, col, guess,board):  # guess is the input being placed in the cell, checking if that guess does not invalidate solution

    row_values = board[row]

    if guess in row_values:
        return False

    col_values = [board[i][col] for i in range(9)]

    if guess in col_values:
        return False

    grid_row = (row // 3) * 3
    grid_col = (col // 3) * 3

    for r in range(grid_row, grid_row + 3):
        for c in range(grid_col, grid_col + 3):
            if board[r][c] == guess:
                return False

    return True


def solve_sudoku(board):
    row, col = find_next_empty(board)  # current empty cell
    if row is None:  # dont have to check if both row and col are None, only need to check one of them
        return True

    for guess in range(1, 10):
        if is_valid(row, col, guess, board):
            board[row][col] = guess

            if solve_sudoku(board):
                return True
        board[row][col] = 0

    return False


if __name__ == '__main__':
    example_board = [
        [0, 0, 0,   0, 8, 0,    0, 0, 3],
        [0, 0, 4,   6, 5, 0,    1, 0, 0],
        [0, 0, 3,   0, 0, 0,    6, 0, 4],

        [0, 0, 0,   0, 0, 0,    3, 0, 2],
        [0, 0, 0,   2, 0, 6,    0, 0, 0],
        [6, 0, 7,   0, 0, 0,    0, 0, 0],

        [7, 0, 1,   0, 0, 0,    9, 0, 0],
        [0, 0, 8,   0, 3, 9,    5, 0, 0],
        [5, 0, 0,   0, 7, 0,    0, 0, 0]
    ]
    print(solve_sudoku(example_board))
    print(example_board)