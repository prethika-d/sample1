N = 8
def is_safe(board, row, col):
    # Check previous rows for column and diagonal conflicts
    for i in range(row):
        # Same column
        if board[i] == col:
            return False
        # Same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False
    return True
def solve_queens(board, row):
    # If all queens are placed
    if row == N:
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            if solve_queens(board, row + 1):
                return True
            board[row] = -1  # Backtrack
    return False
def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
# Main Program
board = [-1] * N
if solve_queens(board, 0):
    print("Solution Found:\n")
    print_board(board)
else:
    print("No Solution Exists")
