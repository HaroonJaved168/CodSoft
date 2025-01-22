import math

# Initialize the game board
def create_board():
    return [" " for _ in range(9)]  # 1D list to represent a 3x3 board

# Print the game board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")

# Check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[cell] == player for cell in condition) for condition in win_conditions)

# Check if the board is full
def is_full(board):
    return " " not in board

# Evaluate the board score for Minimax
def evaluate(board):
    if check_winner(board, "O"):  # AI is "O"
        return 1
    elif check_winner(board, "X"):  # Human is "X"
        return -1
    return 0

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O") or check_winner(board, "X") or is_full(board):
        return evaluate(board)

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI makes a move
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

# Check if the game is over
def is_game_over(board):
    return check_winner(board, "X") or check_winner(board, "O") or is_full(board)

# Main game loop
def play_game():
    board = create_board()
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not is_game_over(board):
        # Human move
        try:
            human_move = int(input("Enter your move (1-9): ")) - 1
            if board[human_move] != " " or not 0 <= human_move < 9:
                print("Invalid move! Try again.")
                continue
            board[human_move] = "X"
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        print_board(board)

        if is_game_over(board):
            break

        # AI move
        print("AI is thinking...")
        ai_move(board)
        print_board(board)

    # Determine the result
    if check_winner(board, "X"):
        print("Congratulations, you win!")
    elif check_winner(board, "O"):
        print("AI wins! Better luck next time.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
