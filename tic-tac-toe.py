board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winner = None
game_running = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")
    
# Take player input
def playerInput(board):
    try:
        i = int(input("Enter a number 1-9: ")) 
        if i >= 1 and i <= 9 and board[i - 1] == "-":
            board[i - 1] = current_player
        else:
            print("This spot is already taken, try again.")
    except ValueError:
        print("Invalid input, please enter a number between 1-9.")

# Check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False
    
def checkTie(board):
    global game_running
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        game_running = False
        
def checkWin():
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}!")
        return True
    return False
    
# Switch the player
def SwitchPlayer():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Game loop
while game_running:
    printBoard(board)
    playerInput(board)
    if checkWin():
        game_running = False
        break
    checkTie(board)
    SwitchPlayer()

    
    
    
    