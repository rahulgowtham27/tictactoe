import math

# Initializing the game board
def init_board():
    return [' ' for _ in range(9)]

# Printing the game board
def print_board(board):
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")
    print("    ")
# Check for a winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]             # Diagonal
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check for a draw
def is_draw(board):
    return ' ' not in board
# Minimax function
def minmax (board, depth, is_maximizing, alpha, beta):# type: ignore
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minmax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minmax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score
# Finding the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minmax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move
def playgame():
    board = init_board()
    current_player = 'X'  # Human starts first

    while True:
        print_board(board)
        
        if current_player == 'X':
            move = int(input("Enter your move (0-8): "))
            if board[move] == ' ':
                board[move] = 'X'
                if check_winner(board, 'X'):
                    print_board(board)
                    print("You win!")
                    break
                current_player = 'O'
        else:
            move = best_move(board)
            board[move] = 'O'# type: ignore
            if check_winner(board, 'O'):
                print_board(board)
                print("AI wins!")
                break
            current_player = 'X'

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
playgame()
