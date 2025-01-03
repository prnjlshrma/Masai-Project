import os

# Function to print the Tic Tac Toe board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("Tic Tac Toe")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all(cell != ' ' for cell in board)

# Function to handle saving the game state
def save_game(board):
    with open('tictactoe_save.txt', 'w') as file:
        file.write(''.join(board))

# Function to handle loading the game state
def load_game():
    if os.path.exists('tictactoe_save.txt'):
        with open('tictactoe_save.txt', 'r') as file:
            board = list(file.read().strip())
            return board
    else:
        return [' '] * 9

# Function to take the player input for their move
def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (1-9 or type 'save' to save the game): ")
        
        # Check if the player wants to save the game
        if move.lower() == 'save':
            save_game(board)
            print("Game saved!")
            continue  # Ask for the move again after saving

        try:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to display the instructions
def display_instructions():
    print("""
    Welcome to Tic Tac Toe!

    Instructions:
    1. The board consists of 9 cells, numbered from 1 to 9, as shown below:
    
       1 | 2 | 3
      ---|---|---
       4 | 5 | 6
      ---|---|---
       7 | 8 | 9
    
    2. Players take turns to enter a number corresponding to the cell they want to place their mark in.
    3. Player X starts first, followed by Player O.
    4. The first player to align three of their marks in a row, column, or diagonal wins!
    5. If the board is full and no player has won, it's a draw.
    6. You can save the game progress at any point by typing 'save'.
    
    Good luck and have fun!
    """)

# Main function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    
    # Display the instructions before starting
    display_instructions()

    # Ask if the player wants to load a saved game
    if input("Do you want to load the saved game? (y/n): ").lower() == 'y':
        board = load_game()
        print("Resuming saved game...")
    else:
        board = [' '] * 9  # Empty board

    # Game loop
    current_player = 'X'
    while True:
        print_board(board)

        # Take the move for the current player
        player_move(board, current_player)

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

    # Offer to restart the game
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        play_game()

if __name__ == "__main__":
    play_game()
