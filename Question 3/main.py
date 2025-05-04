from tictactoe import *

# Display the board nicely
def print_board(board):
    for row in board:
        print("|".join(cell if cell is not None else " " for cell in row))
        print("-" * 5)
    print()

# Main game loop
def play_game():
    board = initial_state()
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The AI is O.")
    print_board(board)

    while not terminal(board):
        current = player(board)

        if current == X:
            print("Your move (enter row and column, e.g., '0 1'):")
            try:
                i, j = map(int, input().split())
                if (i, j) not in actions(board):
                    print("That move is not allowed. Try again.")
                    continue
                board = result(board, (i, j))
            except Exception as e:
                print(f"Invalid input. {e}")
                continue
        else:
            print("AI is thinking...")
            move = minimax(board)
            board = result(board, move)

        print_board(board)

    # Game over
    win = winner(board)
    if win == X:
        print("Congratulations! You win!")
    elif win == O:
        print("The AI wins. Better luck next time!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_game()
