import tkinter

def set_tile(row, column):
    global currentplayer, game_over

    if (game_over):
        return

    if board[row][column]["text"] != "":
        # already taken spot
        return
    
    # Mark the board with the current player's symbol
    board[row][column]["text"] = currentplayer 

    # Set color based on which player is clicking
    if currentplayer == player_x:
        board[row][column].config(foreground=color_red)
    else:
        board[row][column].config(foreground=color_blue)

    # Check for winner BEFORE switching players
    check_winner()

    if not game_over:
        # Switch player
        if currentplayer == player_x:
            currentplayer = player_o
        else:
            currentplayer = player_x
        
        label["text"] = currentplayer + "'s turn"

def check_winner():
    global turns, game_over
    turns += 1

    # Horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_green)
            for column in range(3):
                board[row][column].config(foreground=color_green, background=color_gray)
            game_over = True
            return
    
    # Vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_green)
            for row in range(3):
                board[row][column].config(foreground=color_green, background=color_gray)
            game_over = True
            return
    
    # Diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_green)
        for i in range(3):
            board[i][i].config(foreground=color_green, background=color_gray)
        game_over = True
        return

    # Anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_green)
        board[0][2].config(foreground=color_green, background=color_gray)
        board[1][1].config(foreground=color_green, background=color_gray)
        board[2][0].config(foreground=color_green, background=color_gray)
        game_over = True
        return
    
    # Tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=color_green)

def new_game():
    global turns, game_over, currentplayer

    turns = 0
    game_over = False
    currentplayer = player_x # Reset to X starting

    label.config(text=currentplayer+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

# Constants and Colors
player_x = "X"
player_o = "O"
currentplayer = player_x
turns = 0
game_over = False

color_gray = "#212121"
color_white = "#FCFCFC"
color_red = "#FE4F2D"
color_blue = "#134686"
color_black = "#000000"
color_green = "#6CE800"

# UI Setup
window = tkinter.Tk()
window.title("TTT ni Raf")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame, 
    text=currentplayer + "'s turn",
    font = ("Consolas", 30),
    background = color_black,
    foreground = "white"
    )

label.grid(row=0, column=0, columnspan=3, sticky="we")

# Initialize Board
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", 
                                            font=("Consolas", 70, "bold"),
                                            background=color_gray, 
                                            foreground=color_blue, 
                                            width=4, height=1,
                                            command=lambda row=row, 
                                            column=column: set_tile(row, column)
                                            )    
        board[row][column].grid(row=row+1, column=column)

# Restart Button
button = tkinter.Button(frame, text="RESTART", font=("Consolas", 25), background=color_black,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Center Window Logic
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()