#!/usr/bin/python3

def print_board(board):
    """
    Prints the current game board.
    
    Parameters:
    board (list): A 3x3 list representing the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.
    
    Parameters:
    board (list): A 3x3 list representing the Tic Tac Toe board.
    
    Returns:
    bool: True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Return the winner ('X' or 'O')

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]  # Return the winner ('X' or 'O')

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # Return the winner ('X' or 'O')
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # Return the winner ('X' or 'O')

    return None  # No winner

def tic_tac_toe():
    """
    Main function to play the Tic Tac Toe game.
    Alternates between players 'X' and 'O' and checks for a winner.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        valid_input = False
        while not valid_input:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Validate the row and column input
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input! Row and column must be between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    valid_input = True
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Switch players
        player = "O" if player == "X" else "X"

tic_tac_toe()

