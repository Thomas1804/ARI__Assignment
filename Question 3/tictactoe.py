import copy

# Constants to represent players and empty cells
X = "X"
O = "O"
EMPTY = None

# Start with an empty 3x3 board
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Determine who the current player is (X starts first)
def player(board):
    x_moves = sum(row.count(X) for row in board)
    o_moves = sum(row.count(O) for row in board)
    return X if x_moves == o_moves else O

# Return all available (empty) positions as a set of (row, column) tuples
def actions(board):
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    return possible_moves

# Apply a move to the board and return a new board without changing the original
def result(board, action):
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid move: cell already taken.")
    
    # Copy the board and apply the move
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

# Check if there's a winner (X or O), or return None
def winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    return None

# Check if the game is over (someone won or board is full)
def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

# Give a score: +1 if X wins, -1 if O wins, 0 for a tie
def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

# Minimax algorithm to choose the best move
def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    # Best score for X (maximize)
    def max_value(board):
        if terminal(board):
            return utility(board)
        value = float('-inf')
        for action in actions(board):
            value = max(value, min_value(result(board, action)))
        return value

    # Best score for O (minimize)
    def min_value(board):
        if terminal(board):
            return utility(board)
        value = float('inf')
        for action in actions(board):
            value = min(value, max_value(result(board, action)))
        return value

    best_action = None

    if current_player == X:
        best_score = float('-inf')
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
    else:
        best_score = float('inf')
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action

    return best_action
