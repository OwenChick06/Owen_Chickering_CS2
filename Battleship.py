'''
Name: Owen Chickering
Date: 4/28/25
Project: Battleship
Bugs: N/A
Testers: Penelope S, Julien T
'''


import random

def create_board(board_size):
    return [['🔹' for _ in range(board_size)] for _ in range(board_size)]

def place_ships(board, num_ships):
    board_size = len(board)
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if board[row][col] == '🔹':
            board[row][col] = '🚢'
            ships_placed += 1

def print_board(board, hide_ships=True):
    for row in board:
        for cell in row:
            if hide_ships and cell == '🚢':
                print('🔹', end=' ')
            else:
                print(cell, end=' ')
        print()
    print()

def get_player_move(board):
    while True:
        while True:
            try:
                row = int(input("Enter row: "))
                row = row - 1
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        if 0 <= row < len(board):
            while True:
                col = int(input("Enter column: "))
                col = col - 1
                while True:
                    if 0 <= col < len(board):
                        return row,col
                    else:
                        print("Out of range. Try again.") 
                        break
        else:
            print("Out of range. Try again.")

   
            

def get_computer_move(board):
    while True:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - 1)
        if board[row][col] not in ('🔥', '💦'):
            return row, col

def main():
    while True:
        try:
            board_size = int(input("Select your board size: ")) 
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            while True:
                num_ships = int(input("How many ships do you want: "))
                if 0 <= num_ships <= board_size * board_size:
                    break
                else:
                    print("Input not in range of board")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    player_board   = create_board(board_size)
    computer_board = create_board(board_size)

    place_ships(player_board, num_ships)
    place_ships(computer_board, num_ships)

    turns = board_size * 2  
    player_ships_remaining   = num_ships
    computer_ships_remaining = num_ships

    while turns > 0:
        print("Player board:")
        print_board(player_board, hide_ships=False)
        print("Computer board:")
        print_board(computer_board, hide_ships=True)
        print(f"Turns left: {turns}")

      
        row, col = get_player_move(computer_board)
        if computer_board[row][col] == '🚢':
            print("You hit a ship!")
            computer_board[row][col] = '🔥'
            computer_ships_remaining -= 1
        elif computer_board[row][col] in ('🔥', '💦'):
            print("You already guessed there")
            continue  
        else:
            print("You missed.")
            computer_board[row][col] = '💦'

        if computer_ships_remaining == 0:
            print("You sank all the computer's ships. You win!")
            break

        
        print("Computer's turn...")
        computer_row, computer_col = get_computer_move(player_board)
        if player_board[computer_row][computer_col] == '🚢':
            player_board[computer_row][computer_col] = '🔥'
            player_ships_remaining  -= 1
        else:
            player_board[computer_row][computer_col] = '💦'

        if player_ships_remaining == 0:
            print("The computer sank all your ships. Computer wins!")
            break

        turns -= 1


    if turns == 0 and computer_ships_remaining > 0 and player_ships_remaining > 0:
        print("Game over! You're out of turns.")
        print("Final computer board (ships revealed):")
        print_board(computer_board, hide_ships=False)


main()
