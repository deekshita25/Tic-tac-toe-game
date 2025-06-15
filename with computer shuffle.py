#importing random module
import random

#create empty board
board = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]
currentPlayer = "X"
winner = None
gameRunning = True

#print board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#Take move as input from user
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if inp>=1 and inp<=9:
        if board[inp-1]==' ':
            board[inp-1] = currentPlayer
        elif board[inp-1] != ' ':
            print("Oops player is already at that spot.")
            playerInput(board)
    else:
        print('Invalid Move')
        playerInput(board)

#check if win
def checkWinner(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True
    elif board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[3]
        return True
    elif board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != " ":
        winner = board[2]
        return True

#check for winner and print
def checkIfWin():
    global gameRunning
    if checkWinner(board):
        print(f"The winner is {winner}!")
        printBoard(board)
        gameRunning = False

#check for tie
def checkIfTie(board):
    global gameRunning
    if " " not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

#changing player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#Random moves from computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == " ":
            board[position] = "O"
            switchPlayer()

# Shuffle the entire board after each turn
def shuffleBoard(board):
    random.shuffle(board)  # Shuffle all elements in the list

#Starting the game
while gameRunning:
    print('NEW BOARD')
    printBoard(board)
    checkIfWin()
    while gameRunning==False:
        break
    playerInput(board)
    print('CURRENT BOARD')
    printBoard(board)
    checkIfWin()
    while gameRunning==False:
        break
    checkIfTie(board)
    while gameRunning==False:
        break
    switchPlayer()
    computer(board)
    print('CURRENT BOARD')
    printBoard(board)
    checkIfWin()
    checkIfTie(board)
    shuffleBoard(board)

    
