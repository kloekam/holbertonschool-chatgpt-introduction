#!/usr/bin/python3

def print_board(board):
    
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def board_full(board):
    
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt):
    
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input! Enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def tic_tac_toe():
    
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn")

        # Get valid inputs
        row = get_valid_input("Enter row (0, 1, or 2): ")
        col = get_valid_input("Enter column (0, 1, or 2): ")

        # Ensure cell is empty
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make move
        board[row][col] = player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Run the game
tic_tac_toe()