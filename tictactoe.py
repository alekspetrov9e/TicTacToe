# strategy below

# printing the game board
# take player input
# check for win or tie
# switch the player again
# check for win or tie again

# -----------------------------------------------------
# after having working implementation when computer chooses randomly I will try to make it
# unbeatable using the minimax strategy
import random
board = ["-","-","-"
         ,"-","-","-"
         ,"-","-","-"]
winner = None
currentPlayer = "X"
game_still_running = True

def display_board(example_board):
    for i in range(3):
        print(example_board[3*i] + "|" + example_board[3*i+1] + "|" + example_board[3*i+2])


def take_player_input(example_board):
    print("pick a cell: ",end="")
    while True:
        try:
            input_num = int(input())
        except:
            print("type a number between 0 and 8 ",end="")
        else:
            if 0 <= input_num <= 8 and example_board[input_num] == "-":
                example_board[input_num] = currentPlayer
                break
            else:
                print("the val should be between 0 and 8 and the position free, try again ",end="")


def check_game_over(example_board):
    global winner
    if example_board[0] == example_board[1] == example_board[2] and example_board[1] != "-":
        winner = example_board[0]
        return True

    elif example_board[3] == example_board[4] == example_board[5] and example_board[4] != "-":
        winner = example_board[3]
        return True

    elif example_board[6] == example_board[7] == example_board[8] and example_board[7] != "-":
        winner = example_board[7]
        return True

    elif example_board[0] == example_board[3] == example_board[6] and example_board[3] != "-":
        winner = example_board[3]
        return True

    elif example_board[1] == example_board[4] == example_board[7] and example_board[4] != "-":
        winner = example_board[4]
        return True

    elif example_board[2] == example_board[5] == example_board[8] and example_board[5] != "-":
        winner = example_board[5]
        return True

    elif example_board[0] == example_board[4] == example_board[8] and example_board[4] != "-":
        winner = example_board[4]
        return True

    elif example_board[2] == example_board[4] == example_board[6] and example_board[4] != "-":
        winner = example_board[4]
        return True

    elif "-" not in example_board:
        winner = None
        return True

    else:
        return False

def switch_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = 'O'
    else:
        currentPlayer = "X"

def computer(example_board):
    while True:
        position = random.randint(0, 8)
        if example_board[position] == "-":
            example_board[position] = "O"
            print(f"Computer plays {position}th position")
            switch_player()
            break

display_board(board)
while game_still_running:
    take_player_input(board)
    display_board(board)
    if check_game_over(board):
        if winner is not None:
            if winner == "X":
                print("X won")
            else:
                print("Computer won")
        else:
            print("It is a tie")
        break

    switch_player()
    computer(board)
    display_board(board)
    check_game_over(board)
    if check_game_over(board):
        if winner is not None:
            if winner == "X":
                print("X won")
            else:
                print("Computer won")
        else:
            print("It is a tie")
        break



