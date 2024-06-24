# Define the game board
board = [[' ' for _ in range(10)] for _ in range(10)]

# Define Board & Players
players = ['red', 'yellow']
board_size = 10

# Define the number of rows & columns in the board
num_rows = num_cols = 10 

# Define the Winning Sequence and Empty Cell Length
win_seq_len = 4
empty_cell = ' '

# function to check if a player has won
def check_win(player, board):
    for i in range(num_rows):
        for j in range(num_cols - win_seq_len + 1):
            if all([board[i][j + k] == player for k in range(win_seq_len)]):
                return True
    for i in range(num_rows - win_seq_len + 1):
        for j in range(num_cols):
            if all([board[i + k][j] == player for k in range(win_seq_len)]):
                return True
    for i in range(num_rows - win_seq_len + 1):
        for j in range(num_cols - win_seq_len + 1):
            if all([board[i + k][j + k] == player for k in range(win_seq_len)]):
                return True
    for i in range(num_rows - win_seq_len + 1):
        for j in range(num_cols - win_seq_len + 1):
            if all([board[i + k][j + (win_seq_len - 1) - k] == player for k in range(win_seq_len)]):
                return True
    return False

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-----')

# Switching to Next Player...
def get_next_player(player):
    return players[(players.index(player) + 1) % 2]

# function to check if the board is full
def is_full(board):
    for row in board:
        if empty_cell in row:
            return False
    return True

# Check the number of empty cells in a row
def num_empty_cells(row):
    return row.count(empty_cell)

# function to get the index of the first empty cell 
def first_empty_cell_index(row):
    return row.index(empty_cell)

# function to add a token to the board
def add_token(player, col, board):
    for i in range(num_rows - 1, -1, -1):
        if board[i][col] == empty_cell:
            board[i][col] = player
            break

# The Mini-Max algorithm
def minimax(board, depth, maximizing_player, alpha=float('-inf'), beta=float('inf')):
    if check_win(players[0], board):
        return -1
    if check_win(players[1], board):
        return 1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for col in range(num_cols):
            if num_empty_cells(board[0]) > 0:
                new_board = [row.copy() for row in board]
                add_token(players[0], col, new_board)
                eval = minimax(new_board, depth + 1, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(num_cols):
            if num_empty_cells(board[0]) > 0:
                new_board = [row.copy() for row in board]
                add_token(players[1], col, new_board)
                eval = minimax(new_board, depth + 1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# function to Play Game
def play_game():
    current_player = players[0]
    print_board(board)
    while True:
        column = int(input(f"{current_player}'s turn. Enter column (0-9): "))
        if column < 0 or column >= num_cols or num_empty_cells(board[0]) == 0:
            print("Invalid move. Try again.")
            continue
        add_token(current_player, column, board)
        print_board(board)
        if check_win(current_player, board):
            print(f"{current_player} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        current_player = get_next_player(current_player)

play_game()
