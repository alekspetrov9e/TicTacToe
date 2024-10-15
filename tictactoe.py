board = ["-","-","-"
         ,"-","-","-"
         ,"-","-","-"]
winner = None
currentPlayer = "X"

def print_board(example_board):
    for i in range(3):
        print(example_board[3*i] + "|" + example_board[3*i+1] + "|" + example_board[3*i+2])
print_board(board)