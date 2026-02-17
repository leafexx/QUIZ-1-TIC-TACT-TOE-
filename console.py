import os
#clearing the terminal after the input
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#gameboard
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+-")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+-")
    print(f"{board[6]} | {board[7]} | {board[8]} ")

#check the winner
def check_win(board):
    win_combination = [
        [0, 1, 2],
        [3, 4, 5], 
        [6, 7, 8], 
        [0, 3, 6], 
        [1, 4, 7], 
        [2, 5, 8],
        [0, 4, 8], 
        [2, 4, 6]             
    ]

    for combo in win_combination:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

board = [" " for _ in range(9)]
currentPlayer  = "X"
gameOn = True

print("Welcome to Tic-Tac-Toe")
print("Numbers for taking a spot")
print(f"\n0 | 1 | 2 ")
print("--+---+-")
print("3 | 4 | 5 ")
print("--+---+-")
print("6 | 7 | 8 \n")

#Starting the game
presStart = ""
while presStart.lower() != 's':
    presStart = input("Press S to start the game: ")
    clear_terminal()


# Game loop 
while gameOn:
    display_board(board)
    try:
        choose = int(input(f"Player {currentPlayer} choose a spot (0-8): "))
        clear_terminal()
        
        #invalid input
        if choose < 0 or choose > 8 or board[choose] != " ":
            print("Invalid move! This spot is already taken or out of bounds.")
            continue

        board[choose] = currentPlayer
        clear_terminal()
       
       #Win Game
        winner = check_win(board)
        if winner:
            display_board(board)
            print(f"Congratulations {winner}, you won the game!")
            gameOn = False 

        #Tie Game
        elif " " not in board:
            display_board(board)
            print("It is a Tie")
            gameOn = False

        else:   
            currentPlayer = "O" if currentPlayer == "X" else "X"

    except ValueError:
        clear_terminal()
        print("Please enter a spot between 0 - 8")







