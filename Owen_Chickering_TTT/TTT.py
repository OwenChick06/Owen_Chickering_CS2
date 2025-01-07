# Owen Chickering
# 12/2/24
# Tic Tac Toe
# Some help was recieved by Harrison S to shorten the function used to find a winner



def main(): #Defines the main function
    board = board_game()
    print_board(board) 
    X,O = player() 
    fullbrd(board, X, O) 

def board_game(): #Defines the 2d array for the board
    board = [[1 , 2 , 3 ],
             [4 , 5 , 6 ],
             [7 , 8 , 9 ]]       
    return board

def print_board(board): #This function prints the board in a 3X3 grid
    for row in board: 
        for col in range(len(row)):
            print(row[col],end="")
        print("")
    return board

def player(): #Defines which player is X or O
    print("Player 1 is X")
    X = "X"
    print("Player 2 is O")
    O = "O"
    return (X, O)

def start_gaming(board, X, O, count): #Prompts the active player for their move
    if count == 1 or count == 3 or count == 5 or count == 7 or count == 9: #If player count is odd
        player = X
    elif count == 0 or count == 2 or count == 4 or count == 6 or count == 8 or count == 10: #If player count is even
        player = O
    print(player + " goes now")
    row = int(input("Pick a column:" ))
    col = int(input("Pick a row: "))
    while row > 2 or row < 0 or col > 2 or col < 0: #Out of range of board
        print("Invalid")
        row = int(input("Pick a column: "))
        col = int(input("Pick a row: "))
    while (board[row][col] == X) or (board[row][col] == O): #Spot is filled already
        print("INVALID")
        row = int(input("Pick a column: "))
        col = int(input("Pick a row: "))     
    board[row][col] = player #Replaces the empty spot with X or O
    return (board)

def game_over(board, X, O, count): #This function decides who won
    still_playing = True
    for row in range (0, 2):
        if board[row][0] == board[row][1] == board[row][2]: #scans the rows for winner
            still_playing = False
            print(board[row][0] + " wins") #Prints the winner is that spot
            
    for col in range (0, 2): 
        if board[0][col] == board[1][col] == board[2][col]: #Scans the collumns for winner
            still_playing = False
            print(board[0][col] + " wins") #Prints the winner is that spot

    if board[0][0] == board[1][1] == board[2][2]: #Checks the diagonals for a winner
        still_playing = False
        print(board[0][0] + " wins") #Prints the winner is that spot
    if board[0][2] == board[1][1] == board[2][0]:
        still_playing = False
        print(board[0][2] + " wins") #Prints the winner is said spot
    return still_playing
    
def fullbrd(board, X, O): #This function us used to find when the board is full and if its a tie
    count = 1
    still_playing = True
    while count < 10 and still_playing == True: #While count is less than 10 the game can continue
        start_gaming(board, X, O, count)
        print_board(board)
        if count == 9: #If 9 spots are filled, the board is full
            print("The board is full.")
            if still_playing == True:
                print("There is a tie. ")
        still_playing = game_over(board, X, O, count)
        count += 1 #Adds one to the count
    if still_playing == False:
        print("Game over.")

main() #Calls the main function
