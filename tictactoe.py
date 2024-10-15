# strategy below

# printing the game board
# take player input
# check for win or tie
# switch the player again
# check for win or tie again

import random
board = ["-","-","-"
         ,"-","-","-"
         ,"-","-","-"]
winner = None
currentPlayer = "X"
game_still_running = True

def print_board(example_board):
    for i in range(3):
        print(example_board[3*i] + "|" + example_board[3*i+1] + "|" + example_board[3*i+2])


def take_player_input(example_board):
    while True:
        try:
            input_num = int(input())
        except:
            print("type a number between 0 and 8")
        else:
            if 0 <= input_num <= 8:
                example_board[input_num] = currentPlayer
            else:
                print("the val should be between 0 and 8, try again")


def check_game_over(example_board):
    global winner
    if example_board[0] == example_board[1] == example_board[2] and example_board[1] != "_":
        winner = example_board[0]

    elif example_board[3] == example_board[4] == example_board[5] and example_board[4] != "-":
        winner = example_board[3]

    elif example_board[6] == example_board[7] == example_board[8] and example_board[7] != "-":
        winner = example_board[7]

    elif example_board[0] == example_board[3] == example_board[6] and example_board[3] != "-":
        winner = example_board[3]

    elif example_board[1] == example_board[4] == example_board[7] and example_board[4] != "-":
        winner = example_board[4]

    elif example_board[2] == example_board[5] == example_board[8] and example_board[5] != "-":
        winner = example_board[5]

    elif example_board[0] == example_board[4] == example_board[8] and example_board[4] != "-":
        winner = example_board[4]

    elif example_board[2] == example_board[4] == example_board[6] and example_board[4] != "_":
        winner = example_board[4]
    elif "-" not in example_board:
        winner = None
    else:
        return False

def switch_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = 'O'
    else:
        currentPlayer = "X"

def computer(example_board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if example_board[position] == "-":
            example_board[position] = "O"
            switch_player()

while game_still_running:
    print_board(board)
    take_player_input(board)
    if winner is not None:
        if winner == "X":
            print("X won")
        else:
            print("Computer won")
        break
    switch_player()
    computer(board)
    check_game_over(board)



