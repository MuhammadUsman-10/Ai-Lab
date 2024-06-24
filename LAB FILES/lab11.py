def is_queen(playboard, row, col, N):
    # Check the row on left side
    for i in range(col):
        if playboard[row][i] == 1:
            return False
    
    # Check the upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if playboard[i][j] == 1:
            return False

    # Check the lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if playboard[i][j] == 1:
            return False
    
    return True

def solve_n_queens_problem(playboard, col, N):
    # If all queens are placed then return true
    if col >= N:
        return True

    # Try placing this queen in all rows one by one
    for i in range(N):
        if is_queen(playboard, i, col, N):
            # Place this queen in board[i][col]
            playboard[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens_problem(playboard, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove the queen (backtrack)
            playboard[i][col] = 0

    # If the queen cannot be placed in any row in this column col then return false as no solution exists
    return False

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens_problem(board, 0, N):
        print("No solution exists")
        return False

    print_board(board)
    return True

def print_board(board):
    N = len(board)
    for row in board:
        print(" ".join(str(x) for x in row))
    print("\n")

for N in [4, 8]: 
    print(f"Solving N-Queens Problem when N={N}:")
    solve_n_queens(N)